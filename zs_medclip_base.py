import data_loader.extract_data as extract_data
import data_loader.load_data as load_data
import visualize.visualize as visualize
from zero_shot.clip_classification import CLIPZeroShotClassifier
from zero_shot.medclip_classification import MedCLIPZeroShotClassifier
def run_classification_process_medclip(medical_type, model_type, batch_size):
    """
    Handles the process of running zero-shot classification for medclip and a given medical type.
    :param medical_type: The type of medical data to classify ('ucsd', 'ori').
    :param model_type: The type of model to use for classification ('medclip', 'clip').
    :param batch_size: The batch size for data loading.
    """
    generators, lengths = load_data.create_loader(medical_type, batch_size, model_type)
    visualize.save_random_images_from_generators(generators, [medical_type, model_type, "zs_medclip_base"], 2)
    if model_type == "medclip":
        classifier = MedCLIPZeroShotClassifier(medical_type)
        classifier.run(generators, lengths, "zs_medclip_base")
    else:
        print("Did not define a proper classifer!")

if __name__ == "__main__":
    extract_data.mount_and_process()
    batch_size = 256
    model_types = ['medclip']
    medical_types = ['ucsd', 'ori']
    run_classification_process_medclip(medical_types[0], model_types[0], batch_size)
    run_classification_process_medclip(medical_types[1], model_types[0], batch_size)
