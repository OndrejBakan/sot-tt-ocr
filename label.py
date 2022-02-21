from pylabel import importer

dataset = importer.ImportVOC(path='./runes-yolo')
dataset.exporter.ExportToYoloV5()