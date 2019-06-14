import argparse
import os
import csv
from random import shuffle


class TrainingDataExample:
	def __init__(self, text, category):
		self.text = text,
		self.category = category

class Dataset:

	def writeToDisk(self, fileName, fileContents, outputDir):
		with open(os.path.join(outputDir, fileName), mode='w', encoding='utf-8') as f:
			file_writer = csv.writer(f, delimiter='\t', quotechar='"')
			for each_example in fileContents:
				file_writer.writerow([each_example.text, each_example.category])
		return

	def parse20NG(self, inputDir, outputDir, train=True):
		if train:
			classes = []
			train_set = []
			dev_set = []
			try:
				for folder in os.listdir(inputDir):
					classes.append(folder)
					examples = []
					for DataFile in os.listdir(os.path.join(inputDir, folder)):
						try:
							trainFile = open(os.path.join(inputDir, folder, DataFile), mode='r', encoding='utf-8').readlines()
							trainFile = ' '.join(trainFile)
							examples.append(TrainingDataExample(trainFile, folder))
						except Exception as e:
							print("Warning Message " + str(e))
					shuffle(examples)
					number_of_examples = len(examples)
					train_set += examples[:int(number_of_examples*0.8)]
					dev_set += examples[int(number_of_examples*0.8):]
			except Exception as e:
				print("Warning Message " + str(e))
			
			self.writeToDisk("train.tsv", train_set, outputDir)
			self.writeToDisk("dev.tsv", dev_set, outputDir)
		else:
			try:
				examples = []
				for folder in os.listdir(inputDir):
					for DataFile in os.listdir(os.path.join(inputDir, folder)):
						try:
							trainFile = open(os.path.join(inputDir, folder, DataFile), mode='r', encoding='utf-8').readlines()
							trainFile = ' '.join(trainFile)
							examples.append(TrainingDataExample(trainFile, folder))
						except Exception as e:
							print("Warning Message " + str(e))
			except Exception as e:
				print("Warning Message " + str(e))
			shuffle(examples)
			self.writeToDisk("test.tsv", examples, outputDir)
		return

def main():
	parser = argparse.ArgumentParser()

	##Required Parameters
	parser.add_argument("--train_dir",
						default=None,
						type=str,
						required=True,
						help="Input train dir")
	parser.add_argument("--test_dir",
						default=None,
						type=str,
						required=True,
						help="Input test dir")				

	parser.add_argument("--output_dir",
						default=None,
						type=str,
						required=True,
						help="Output dir")
	
	parser.add_argument("--task_name",
						choices=['20NG'],
						required=True,
						type=str,
						help='Type of the dataset processing')
	args = parser.parse_args()
	dataset = Dataset()
	dataset.parse20NG(args.train_dir, args.output_dir, True)
	dataset.parse20NG(args.test_dir, args.output_dir, False)

if __name__ == '__main__':
	main()
