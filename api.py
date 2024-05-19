from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import StoppingCriteria, StoppingCriteriaList


model = AutoModelForCausalLM.from_pretrained("OpenELM-270M-Instruct", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", token="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")
# Set the pad_token as eos_token
tokenizer.pad_token = tokenizer.eos_token
MAX_OUTPUT_TOKENS = 200

# stopping criteria class
class StopOnNewLine(StoppingCriteria):
    def __call__(self, input_ids, scores, **kwargs):
        # Check if the last token is a newline character
        if input_ids[0][-1] == tokenizer.encode("\n", add_special_tokens=False)[-1]:
            return True
        return False

def predict(prompt, temperature):
    try:
        # Encode the prompt and create attention mask
        inputs = tokenizer(prompt, return_tensors="pt", padding=True)
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask
        
        # Generate text with early stopping criteria
        stopping_criteria = StoppingCriteriaList([StopOnNewLine()])
        outputs = model.generate(input_ids,
                                attention_mask=attention_mask,
                                max_new_tokens=MAX_OUTPUT_TOKENS,
                                pad_token_id=tokenizer.eos_token_id,
                                stopping_criteria=stopping_criteria,
                                do_sample=True,  # Enable sampling
                                temperature=temperature,  # Adjust temperature for randomness
                                top_k=50,  # Top-k sampling
                                top_p=0.95,  # Top-p sampling
                                )

        # Decode the output
        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        output_text = output_text[len(prompt):]
        return output_text.strip()
    
    except Exception as error:
        print(error)
        result = {
            'error': {
                'code': getattr(error, 'code', 'Unknown'),
                'message': str(error)
            }
        }
        return result
        