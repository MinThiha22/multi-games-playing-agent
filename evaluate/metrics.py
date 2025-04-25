class EvaluationMetrics:
  def __init__(self):
    self.nodes_explored = 0
    self.execution_time = 0
    self.prune_count = 0
  
  def display(self):
    print("Nodes Explored:", self.nodes_explored)
    print(f"Execution Time: {self.execution_time:.4f} seconds"), 
    