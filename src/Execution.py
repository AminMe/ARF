from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.classification.lazy.knn_adwin import KNNAdwin, KNN
from skmultiflow.options.file_option import FileOption
from skmultiflow.data.file_stream import FileStream
from src.AdaptiveRandomForest import AdaptiveRandomForest
from skmultiflow.classification.meta.leverage_bagging import LeverageBagging

dataset = "poker"

# 1. Create a stream
opt = FileOption("FILE", "OPT_NAME", dataset+".csv", "CSV", False)
stream = FileStream(opt, -1, 1)
# 2. Prepare for use
stream.prepare_for_use()
# 2. Instantiate the HoeffdingTree classifier

h = [
        #LeverageBagging(h=KNN(), ensemble_length=2),
        HoeffdingTree(),
        AdaptiveRandomForest(m=25, n=100),
     ]
# 3. Setup the evaluator
eval1 = EvaluatePrequential(pretrain_size=1000, output_file='result_'+dataset+'.csv', max_instances=10000, batch_size=1, n_wait=500, max_time=1000000000, task_type='classification', show_plot=False, plot_options=['performance'])
# 4. Run
eval1.eval(stream=stream, classifier=h)
