"""
Evaluation Metrics for Information Retrieval
"""
import numpy as np
from typing import Dict, List


class IRMetrics:
    """Information Retrieval evaluation metrics."""
    
    @staticmethod
    def recall_at_k(results: Dict[int, List[int]], qrels: Dict[int, Dict[int, int]], k: int) -> float:
        """
        Calculate Recall@k: fraction of relevant documents found in top-k.
        
        Args:
            results: {query_id: [doc_ids]}
            qrels: {query_id: {doc_id: relevance_score}}
            k: cutoff for top-k evaluation
        """
        recall_scores = []
        for q_id in results:
            if q_id not in qrels:
                continue
            
            # YOUR CODE HERE: Calculate recall for this query
            top_k_retrieved = results[q_id][:k]

            actual_relevant = {doc_id for doc_id, score in qrels[q_id].items() if score > 0}

            if not actual_relevant:
                continue


            hits = sum(1 for doc_id in top_k_retrieved if doc_id in actual_relevant)

            query_recall = hits /  len(actual_relevant)
            recall_scores.append(query_recall)
            
        return float(np.mean(recall_scores)) if recall_scores else 0.0

    @staticmethod
    def precision_at_k(results: Dict[int, List[int]], qrels: Dict[int, Dict[int, int]], k: int) -> float:
        """
        Calculate Precision@k: fraction of top-k that are relevant.
        """
        precision_scores = []
        for q_id in results:
            if q_id not in qrels:
                continue
            
            # YOUR CODE HERE: Calculate precision for this query
            top_k_retrieved = results[q_id][:k]

            if k == 0:
                return 0.0

            actual_relevant = {doc_id for doc_id, score in qrels[q_id].items() if score > 0}

            hits = sum(1 for doc_id in top_k_retrieved if doc_id in actual_relevant)

            query_precision = hits / k
            precision_scores.append(query_precision)

            
        return float(np.mean(precision_scores)) if precision_scores else 0.0

    @staticmethod
    def mrr(results: Dict[int, List[int]], qrels: Dict[int, Dict[int, int]]) -> float:
        """
        Calculate Mean Reciprocal Rank (MRR).
        """
        reciprocal_ranks = []
        for q_id in results:
            if q_id not in qrels:
                continue
            
            # YOUR CODE HERE: Calculate MRR for this query
            retrieved_docs = results[q_id]
            actual_relevant = {doc_id for doc_id, score in qrels[q_id].items() if score > 0} 

            if not actual_relevant:
                continue

            found_relevant = False
            for rank_idx, doc_id in enumerate(retrieved_docs):
                if doc_id in actual_relevant:
                    rank = rank_idx + 1
                    reciprocal_ranks.append(1 / rank)
                    found_relevant = True
                    break

            if not found_relevant:
                reciprocal_ranks.append(0.0)

            
        return float(np.mean(reciprocal_ranks)) if reciprocal_ranks else 0.0

    @staticmethod
    def evaluate_retrieval(results: Dict[int, List[int]], qrels: Dict[int, Dict[int, int]]) -> Dict[str, float]:
        """
        Comprehensive evaluation with standard IR metrics.
        
        Returns:
            Dictionary with metric names and values
        """
        metrics = {
            'Recall@1': IRMetrics.recall_at_k(results, qrels, 1),
            'Recall@5': IRMetrics.recall_at_k(results, qrels, 5), 
            'Recall@10': IRMetrics.recall_at_k(results, qrels, 10),
            'Precision@5': IRMetrics.precision_at_k(results, qrels, 5),
            'MRR': IRMetrics.mrr(results, qrels)
        }
        return metrics

    @staticmethod
    def print_metrics(metrics: Dict[str, float], title: str = "Evaluation Results"):
        """Pretty print evaluation metrics."""
        print(f"\n📊 {title}")
        print("=" * 40)
        for metric, value in metrics.items():
            print(f"{metric:12}: {value:.4f}")
        print("=" * 40)
