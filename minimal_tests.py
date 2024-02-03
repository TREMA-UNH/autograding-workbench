# from pathlib import Path
# from typing import Dict, List
# from exam_pp.exam_cover_metric import compute_exam_cover_scores, write_exam_results, ExamCoverScorerFactory
# from exam_pp.parse_qrels_runs_with_text import GradeFilter, QueryWithFullParagraphList, parseQueryWithFullParagraphs


from exam_pp import exam_grading, exam_post_pipeline


exam_grading.main(cmdargs=["./benchmarkY3test-exam-qrels-runs-with-text.jsonl.gz"
                           ,"-o","result.jsonl.gz"
                           ,"--model-pipeline", "text2text"
                           ,"--model-name","google/flan-t5-base"
                           ,"--prompt-class","QuestionCompleteConcisePromptWithAnswerKey"
                           ,"--question-path","./tqa_train_val_test"
                           ,"--max-queries","1","--max-paragraphs","1","--question-type", "tqa"
                           ])


#python -m exam_pp.exam_grading  -o result.jsonl.gz  ./benchmarkY3test-exam-qrels-runs-with-text.jsonl.gz--model-pipeline text2text --model-name google/flan-t5-large --prompt-class QuestionCompleteConcisePromptWithAnswerKey tqa --question-path ./tqa_train_val_test --question-type tqa

print("\n\n\n\n\n\n")

# exam_grading.main(cmdargs=["./dl19-qrels-with-text.jsonl.gz"
#                            ,"--run-dir","./run-dl"
                           # ,"-o","result.jsonl.gz"
#                            ,"--model-pipeline", "text2text"
#                            ,"--model-name","google/flan-t5-base"
#                            ,"--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
#                            ,"--max-queries","1","--max-paragraphs","1","--question-type"
#                            ,"question-bank","--question-path","./dl19-questions.jsonl.gz"
#                            ])




car_graded_file = "./t5-rating-naghmehs-tqa-exam-qrel-runs-result-T0050.jsonl.gz"
dl_graded_file = "dl19-exam-qrels-with-text.jsonl.gz"

# exam_post_pipeline.main(cmdargs=[dl_graded_file
#                               ,"-q","out.qrel"
#                               ,"--run-dir","./run-dl","--qrel-query-facets", "--use-ratings"
#                               , "--model","google/flan-t5-large","--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices" 
#                               , "--question-set", "question-bank"
#                               , "--testset","dl19"
#                               , "-r"
#                               , '--official-leaderboard', 'faux-leaderboard.json'
#                               ])


# exam_post_pipeline.main(cmdargs=[dl_graded_file,
#                                  "--correlation-out","out.correlation.tex"
#                                  ,"--model","google/flan-t5-large","--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
#                               , "--question-set", "question-bank"
#                               , "--testset","dl19"
#                               ,"--use-ratings"
#                               , '--official-leaderboard', 'faux-leaderboard.json'
#                                 ])

# exam_post_pipeline.main(cmdargs=[dl_graded_file 
#                                  ,"--leaderboard-out","out.leaderboard.tsv"
#                                  ,"--model","google/flan-t5-large","--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
#                               , "--question-set", "question-bank"
#                               , "-r", "--min-self-rating","4"
#                               , "--testset","dl19"
#                               , '--official-leaderboard', 'faux-leaderboard.json'
#                               ])

# exam_post_pipeline.main(cmdargs= [car_graded_file ,"--leaderboard-out","out.leaderboard.tsv","--model","google/flan-t5-large","--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices", 
#                                "--question-set", "tqa", "-r", "--min-self-rating","4"])



print("\n\n\n\n\n\n")




exam_grading.main(cmdargs=["./benchmarkY3test-exam-qrels-runs-with-text.jsonl.gz"
                     ,"-o","result.jsonl.gz"
                     ,"--model-pipeline", "text2text"
                     ,"--model-name","google/flan-t5-base"
                     ,"--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
                     ,"--max-queries","1","--max-paragraphs","1"
                     ,"--question-type","naghmeh","--question-path","naghmeh-questions.json"
                     ])

print("\n\n\n\n\n\n")



exam_grading.main(cmdargs=["./benchmarkY3test-exam-qrels-runs-with-text.jsonl.gz"
                           ,"-o","result.jsonl.gz"
                           ,"--model-pipeline", "text2text"
                           ,"--model-name","google/flan-t5-base"
                           ,"--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
                           ,"--max-queries","1","--max-paragraphs","1"
                           ,"--question-type","question-bank"
                           ,"--question-path","newfile.json.gz"])
print("\n\n\n\n\n\n")



exam_grading.main(["./benchmarkY3test-exam-qrels-runs-with-text.jsonl.gz"
                           ,"-o","result.jsonl.gz"
                           ,"--model-pipeline", "text2text"
                           ,"--model-name","google/flan-t5-base"
                           ,"--prompt-class","QuestionSelfRatedUnanswerablePromptWithChoices"
                           ,"--max-queries","1","--max-paragraphs","1"
                           ,"--question-type","question-bank"
                           ,"--question-path","newfile.json.gz"])


#  result_trecDL2019-qrels-with-text__new_subqueries_v2__large.jsonl.gz