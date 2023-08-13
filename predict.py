import datetime
import os
from datetime import time

import torch
import time

from parser_model import ParserModel
from parser_transitions import PartialParse
from utils.parser_utils import load_and_preprocess_data


import os
import torch
import time
from datetime import datetime
from parser_model import ParserModel
from utils.parser_utils import load_and_preprocess_data

def main():
    parser, embeddings, _, _, test_data = load_and_preprocess_data(False)  # 设置 debug 参数为 False
    start = time.time()
    model = ParserModel(embeddings)
    parser.model = model
    print("Model initialized in {:.2f} seconds\n".format(time.time() - start))

    print("=" * 80)
    print("PREDICTION")
    print("=" * 80)

    # 加载之前训练好的模型权重
    output_path = "/Users/doge/Documents/Stanford Summer/CS224/student/results/20230807_094944/model.weights"
    if os.path.exists(output_path):
        print("Restoring the model weights")
        parser.model.load_state_dict(torch.load(output_path))
    else:
        print("Model weights not found. Please train the model first.")
        return

    # 设置模型为评估模式并进行预测
    parser.model.eval()
    UAS, dependencies = parser.parse(test_data)  # 仅进行预测，不计算 UAS

    print("Prediction done!")
    print(dependencies)
    print(UAS)
if __name__ == "__main__":
    main()


