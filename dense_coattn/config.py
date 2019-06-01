
import argparse


def get_train_config():
	parser = argparse.ArgumentParser()

	arch = parser.add_argument_group("Model Architecture")
	arch.add_argument("--arch", default="DCNWithRCNN")
	arch.add_argument("--num-layers", type=int, default=2)
	arch.add_argument("--cnn-name", type=str, default="resnet152")
	arch.add_argument("--img-size", type=int, default=2048)
	arch.add_argument("--ques-size", type=int, default=1024)
	arch.add_argument("--num-img-attn", type=int, default=4)
	arch.add_argument("--num-dense-attn", type=int, default=4)
	arch.add_argument("--num-predict-attn", type=int, default=4)
	arch.add_argument("--num-none", type=int, default=3)
	arch.add_argument("--num-seq", type=int, default=5)
	arch.add_argument("--word-vectors", type=str, default="/home/duykien/storage/vqa/dataset/glove_840B.pt")
	arch.add_argument("--droprnn", type=float, default=0.1)
	arch.add_argument("--dropout", type=float, default=0.3)

	train = parser.add_argument_group("Training Setup")
	train.add_argument("--num-epoch", type=int, default=25)
	train.add_argument("--num-iter", type=int, default=-1)
	train.add_argument("--patience", type=int, default=5)
	train.add_argument("--trainval", type=int, default=0)
	train.add_argument("--data-path", type=str, default="/home/duykien/storage/vqa/dataset")
	train.add_argument("--data-name", type=str, default="cocotrain")
	train.add_argument("--img-path", type=str, default="/home/duykien/storage/vqa/image")
	train.add_argument("--img-type", type=str, default="rcnn")

	optim = parser.add_argument_group("Optimizer Config")
	optim.add_argument("--max-grad-norm", type=float, default=-1)
	optim.add_argument("--lr", type=float, nargs="+", default=[0.001])
	optim.add_argument("--lr-shrink", type=float, default=0.5)
	optim.add_argument("--warmup-init-lr", type=float, default=0.001)
	optim.add_argument("--warmup-updates", type=float, default=0)
	optim.add_argument("--step-size", type=int, default=7)
	optim.add_argument("--weight-decay", type=float, default=0.0001)
	optim.add_argument("--adam-betas", default="(0.9, 0.999)")
	optim.add_argument("--adam-eps", type=float, default=1e-08)
	optim.add_argument("--no-record", action="store_false", dest="record", default=True)

	evaluate = parser.add_argument_group("Evaluation Mode")
	evaluate.add_argument("--ann-file", default='/home/duykien/storage/vqa/dataset/v2_mscoco_val2014_annotations.json')
	evaluate.add_argument("--ques-file",  default='/home/duykien/storage/vqa/dataset/v2_OpenEnded_mscoco_val2014_questions.json')
	evaluate.add_argument("--result-file", default='/home/duykien/storage/vqa/result')

	general = parser.add_argument_group("General Setup")
	general.add_argument("--resume", default=None)
	general.add_argument("--no-overwrite", action="store_false", dest="overwrite", default=True)
	general.add_argument("--use-thread", action="store_true")
	general.add_argument("--use-tensorboard", action="store_true")
	general.add_argument("--size-scale", default=(448, 448))
	general.add_argument("--directory", type=str, default="/home/duykien/storage/vqa/model")
	general.add_argument("--model", type=str, default="DCN0")
	general.add_argument("--gpus", type=int, nargs="+", default=[0, 1, 2, 3])
	general.add_argument("--log-interval", type=int, default=100)
	general.add_argument("--save-freq", type=int, default=10)
	general.add_argument("--seed", type=int, default=12345)
	general.add_argument("--num-workers", type=int, default=4)
	general.add_argument("--batch-size", type=int, default=400)
	
	return parser.parse_args()


def get_answer_config():
	parser = argparse.ArgumentParser()

	arch = parser.add_argument_group("Model Architecture")
	arch.add_argument("--arch", default="DCN")
	arch.add_argument("--num-layers", type=int, default=2)
	arch.add_argument("--cnn-name", type=str, default="resnet152")
	arch.add_argument("--img-size", type=int, default=2048)
	arch.add_argument("--ques-size", type=int, default=1024)
	arch.add_argument("--num-img-attn", type=int, default=4)
	arch.add_argument("--num-dense-attn", type=int, default=4)
	arch.add_argument("--num-predict-attn", type=int, default=4)
	arch.add_argument("--num-none", type=int, default=3)
	arch.add_argument("--num-seq", type=int, default=5)
	arch.add_argument("--word-vectors", type=str, default="/home/duykien/storage/vqa/dataset/glove_840B.pt")
	arch.add_argument("--droprnn", type=float, default=0.1)
	arch.add_argument("--dropout", type=float, default=0.3)

	general = parser.add_argument_group("General Setup")
	general.add_argument("--resume", default=None)
	general.add_argument("--use-thread", action="store_true")
	general.add_argument("--size-scale", default=(448, 448))
	general.add_argument("--directory", type=str, default="/home/duykien/storage/vqa/model")
	general.add_argument("--model", type=str, default="DCN0")
	general.add_argument("--gpus", type=int, nargs="+", default=[0, 1, 2, 3])
	general.add_argument("--log-interval", type=int, default=100)
	general.add_argument("--seed", type=int, default=12345)
	general.add_argument("--num-workers", type=int, default=4)
	general.add_argument("--batch-size", type=int, default=400)

	answer = parser.add_argument_group("Answer Setup")
	answer.add_argument("--data-path", type=str, default="/home/duykien/storage/vqa/dataset")
	answer.add_argument("--data-name", type=str, default="cocotrain")
	answer.add_argument("--img-path", type=str, default="/home/duykien/storage/vqa/image")
	answer.add_argument("--img-type", type=str, default="rcnn")
	answer.add_argument("--save-file", type=str, default="")
	answer.add_argument("--ensemble", action="store_true")
	
	return parser.parse_args()