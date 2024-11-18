from bert_score import BERTScorer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def score(lang : str, model_type : str, candidate_sentences : list[str], reference_sentences : list[str]) -> dict:
    """
    wrapper function to get precision, recall and f1 of candidate_sentences with respect to reference_sentences using bert models
    """
    try:
        scorer = BERTScorer(lang=lang, model_type=model_type)
        precision, recall, f1 = scorer.score(candidate_sentences, reference_sentences)
        return {
            "success" : True,
            "data" : {
                "precision" : precision,
                "recall" : recall,
                "f1" : f1
            },
            "error" : None
        }
    except Exception as e:
        logger.error(f"score fn could not compute score error :  {e}")
        return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }

