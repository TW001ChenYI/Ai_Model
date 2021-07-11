import tensorflow as tf
import application.ai_model
def generate_text(model, start_string,num_generate,temperature): 
  # Number of characters to generate
    num_generate = int(num_generate)
    input_eval = application.ai_model.tokenizer.texts_to_sequences([start_string])[0]
    input_eval = tf.expand_dims(input_eval, 0)
    # Empty string to store our results
    text_generated = []
    temperature = float(temperature)
    
    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)
        # using a categorical distribution to predict the character returned by the model 
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions,
        num_samples=1)[-1,0].numpy()
        # We pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(application.ai_model.tokenizer.index_word[predicted_id])
    return (start_string + ''.join(text_generated))


