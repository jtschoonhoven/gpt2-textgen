"""
Based on README usage example from https://github.com/minimaxir/gpt-2-simple.
View gpt_2_simple source at https://github.com/minimaxir/gpt-2-simple/blob/master/gpt_2_simple/gpt_2.py
"""
import argparse
import gpt_2_simple as gpt2
import os
from tensorflow.compat.v1 import Session as TfSession


MODEL_NAME = '124M'
DEFAULT_FILE_PATH_INPUT = './example_input.txt'
DEFAULT_TRAINING_STEPS = 3
DEFAULT_CHAR_LENGTH = 1024
DEFAULT_CREATIVITY = 0.7


"""
Configure and generate the models used to generate text output.
"""
def train(
    tf_session: TfSession,
    file_path_input: str = DEFAULT_FILE_PATH_INPUT,
    training_steps: int = DEFAULT_TRAINING_STEPS,
) -> None:
    if not os.path.isdir(os.path.join('models', MODEL_NAME)):
        print(f'Downloading { MODEL_NAME } model...')
        gpt2.download_gpt2(model_name=MODEL_NAME)

    gpt2.finetune(
        tf_session,
        file_path_input,
        model_name=MODEL_NAME,
        steps=training_steps,
    )

    return tf_session


"""
Generate text based on a previously-trained model loaded into tf_session.
"""
def generate(
    tf_session: TfSession,
    creativity: float = DEFAULT_CREATIVITY,
    length: int = DEFAULT_CHAR_LENGTH,
    prefix: str = None,
) -> None:
    gpt2.generate(
        tf_session,
        length=length,
        temperature=creativity,
        prefix=prefix,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-path-input', '-f', default=DEFAULT_FILE_PATH_INPUT)
    parser.add_argument('--retrain', '-r', type=bool, default=False)
    parser.add_argument('--length', '-l', type=int, default=DEFAULT_CHAR_LENGTH)
    parser.add_argument('--training-steps', '-s', type=int, default=DEFAULT_TRAINING_STEPS)
    parser.add_argument('--creativity', '-c', type=float, default=DEFAULT_CREATIVITY)
    parser.add_argument('--prefix', '-p')
    args = parser.parse_args()

    should_train: bool = args.retrain
    tf_session = gpt2.start_tf_sess()

    try:
        gpt2.load_gpt2(tf_session)
    except FileNotFoundError:
        should_train = True

    if should_train:
        train(
            tf_session,
            file_path_input=args.file_path_input,
            training_steps=args.training_steps,
        )

    generate(
        tf_session,
        creativity=args.creativity,
        length=args.length,
        prefix=args.prefix,
    )
