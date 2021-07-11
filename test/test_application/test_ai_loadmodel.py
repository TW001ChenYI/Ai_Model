import test_application.test_ai_model

import tensorflow as tf

h5_path='Model/my_Model_6books_44Words_150Epochs.h5'
test_application.test_ai_model.infer_model.load_weights(h5_path)
test_application.test_ai_model.infer_model.build(
    tf.TensorShape([1, None]))