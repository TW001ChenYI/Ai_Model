import tensorflow as tf

import test_application.test_text

w = len(set(test_application.test_text.text))
tokenizer = tf.keras.preprocessing.text.Tokenizer(
        num_words=w,char_level=True,filters='')
tokenizer.fit_on_texts(test_application.test_text.text)
EMBEDDING_DIM = 512
RNN_UNITS = 1024
BATCH_SIZE = 1
# 專門用來做生成的模型容器
infer_model = tf.keras.Sequential()
# 詞嵌入層
infer_model.add(
    tf.keras.layers.Embedding(
        input_dim=w, 
        output_dim=EMBEDDING_DIM,
        batch_input_shape=[BATCH_SIZE, None]
        ))
# LSTM 層
infer_model.add(tf.keras.layers.LSTM(units=RNN_UNITS, return_sequences=True, stateful=True))
# 全連接層
infer_model.add(tf.keras.layers.Dense(w))
infer_model.build(tf.TensorShape([1, None]))



