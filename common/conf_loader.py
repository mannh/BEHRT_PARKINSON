import json
from pathlib import Path


class ConfLoader:
    def __init__(self, path):
        self.path = Path(path)

    def load_configs(self, file_name):
        with open(self.path / file_name, 'r') as fh:
            return json.load(fh)

    def load_train_params(self, file_name, global_params):
        configs = self.load_configs(file_name)
        configs['max_len_seq'] = global_params['max_seq_len']
        return configs

    def load_model_configs(self, file_name, global_params, BertVocab, ageVocab):
        configs = self.load_configs(file_name)
        configs['vocab_size'] = len(BertVocab['token2idx'].keys())
        configs['age_vocab_size'] = len(ageVocab.keys())
        configs['max_position_embedding'] = global_params['max_len_seq']
        return configs


