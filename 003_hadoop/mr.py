def mapper(input_key, input_value, writer):
    # your computation here
    writer.emit(intermediate_key, intermediate_value)

def reducer(intermediate_key, value_iterator, writer):
    # your computation here
    writer.emit(output_key, output_value)
