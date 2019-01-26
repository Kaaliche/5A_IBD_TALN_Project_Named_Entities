from sklearn.metrics import classification_report

from ner.document import Vectorizer
from ner.parser import EnglishNerParser
from ner.parser.parser import SimpleTextParser
import os
from keras.utils import np_utils
from keras.callbacks import TensorBoard, EarlyStopping, ModelCheckpoint
from ner.neuralNetwork.recurrentNeuralNetwork import RecurrentNeuralNetwork
from ner.data import DATA_DIR

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

print("Reading training data")
test_file = os.path.join(DATA_DIR, 'files', 'eng.test.txt')
glove_file = os.path.join(DATA_DIR, 'files', 'glove.6B.50d.txt')
documents = EnglishNerParser().read_file(test_file)


print("Create features")
vectorizer = Vectorizer(word_embedding_path=glove_file)
word, pos, shape = vectorizer.encode_features(documents)
labels = vectorizer.encode_annotations(documents)
print("Loaded {} data samples".format(len(labels)))

split = int(len(word)*80/100)
word_train, word_validation = word[0:split], word[split:]
pos_train, pos_validation = pos[0: split], pos[split:]
shape_train, shape_validation = shape[0: split], shape[split:]

y_train, y_validation = [labels[0: split]], [labels[split:]]
tb_callback = TensorBoard("./logs/lstm")
print('Building network...')
model = RecurrentNeuralNetwork.build_classification(word_embeddings=vectorizer.word_embedding,
                                            input_shape={'pos': (len(vectorizer.pos2index), 10),
                                                         'shape': (len(vectorizer.shape_dictionnary), 2)},
                                            out_shape=len(vectorizer.labels_dictonnary),
                                            units=100, dropout_rate=0.5)

print('Train...')
trained_model_name = 'ner_weights.h5'

# Callback that stops training based on the loss fuction
early_stopping = EarlyStopping(monitor='val_loss', patience=10)

# Callback that saves the best model across epochs
saveBestModel = ModelCheckpoint(trained_model_name, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

x_train = [word_train, pos_train, shape_train]
x_validation = [word_validation, pos_validation, shape_validation]

model.fit(x_train, y_train,
          validation_data=([word_validation, pos_validation, shape_validation], y_validation),
          batch_size=32,  epochs=10, callbacks=[saveBestModel, early_stopping, tb_callback])

# Load the best weights in the model
model.load_weights(trained_model_name)

# Save the complete model
model.save('rnn.h5')

# Use the test data: Unpadded feature vectors + unpaded and numerical (not one-hot vectors) labels

predict = model.predict([word_validation, pos_validation, shape_validation], batch_size = 5)

predict = [RecurrentNeuralNetwork.probas_to_classes(p) for p in predict]

accuracy = sum([1 for p, l in zip(predict, y_validation) if p == l]) / word_validation.shape[0]


# For each sample (one at a time)
    # Predict labels and convert from probabilities to classes
    # RecurrentNeuralNetwork.probas_to_classes()

print(classification_report(y_validation, predict))