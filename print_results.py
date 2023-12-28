#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Xiaoqing (Lexi) Li
# DATE CREATED: 12/23/2023
# REVISED DATE: 12/24/2023
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
## 

#import pandas as pd
from calculates_results_stats import pct

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    ###
    """ reminder of what dict: results_stats_dic items are
    results_stats_dic["n_images"] =  Z # - number of images
    results_stats_dic["n_correct_dogs"] =  A # - number of correctly classified dog images
    results_stats_dic["n_dogs_img"] =  B # - number of dog images
    results_stats_dic["n_correct_notdogs"] =  C # - number of correctly classified NON-dog images
    results_stats_dic["n_notdogs_img"] =  D # - number of NON-dog images
    results_stats_dic["n_correct_breed"] =  E # - number of correctly classified dog breeds
    results_stats_dic["n_match"] =  Y # - number of matched breed
    results_stats_dic["pct_match"] =  pct(Y,Z) # - percentage of correct matches
    results_stats_dic["pct_correct_dogs"] =  pct(A,B) # - percentage of correctly classified dogs
    results_stats_dic["pct_correct_breed"] =  pct(E,B) # - percentage of correctly classified dog breeds
    results_stats_dic["pct_correct_notdogs"] =  pct(C,D) # - percentage of correctly classified NON-dogs
    """
    ### print results required by the project
    print("\n\n")
    
    print("----------------------------------------------------------------------------------")
    print("*** Results Summary for CNN Model Architecture ",model.upper(), "***")
    print("----------------------------------------------------------------------------------")
    print("\n\n")
    
    print("{:>35}: {:>3d}".format('N Images', results_stats_dic['n_images'])) # Z
    print("{:>35}: {:>3d}".format('N Dog Images', results_stats_dic['n_dogs_img'])) # B
    print("{:>35}: {:>3d}".format('N NON-Dog Images', results_stats_dic['n_notdogs_img'])) # D #Uncomment this line because n_notdogs_img is the 3rd stat you need to display here.
    print("\n")
    print("{:>35}: {:>6.2f}%".format('pct_match', results_stats_dic['pct_match'])) # pct(Y,Z) # - percentage of correct matches
    print("{:>35}: {:>6.2f}%".format('pct_correct_dogs', results_stats_dic['pct_correct_dogs'])) # pct(A,B) # - percentage of correctly classified dogs
    print("{:>35}: {:>6.2f}%".format('pct_correct_breed', results_stats_dic['pct_correct_breed'])) # pct(E,B) # - percentage of correctly classified dog breeds
    print("{:>35}: {:>6.2f}%".format('pct_correct_notdogs', results_stats_dic['pct_correct_notdogs'])) #  pct(C,D) # - percentage of correctly classified NON-dogs
    
    ### print incorrect dogs info
    n_incorrect_dogs = results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] - results_stats_dic["n_images"]
    if print_incorrect_dogs and n_incorrect_dogs != 0 : # - True prints incorrectly classified dog images
        print("\n\n")
        print("Incorrectly-classified dog images:")
        count = 0
        for file_name in results_dic.keys():
            if sum(results_dic[file_name][3:]) == 1:
                print("{} is{} a dog, but is classified as{} a dog.".format(file_name,[' not',''][results_dic[file_name][3]],[' not',''][results_dic[file_name][4]]))
                count += 1
        #if not count: # count==0
        #    print("None")
        
    # print incorrect breed info
    n_incorrect_breed = results_stats_dic['n_correct_dogs'] - results_stats_dic['n_correct_breed']
    if print_incorrect_breed and n_incorrect_breed !=0 : # - True prints incorrectly classified dog breeds
        print("\n\n")
        print("Incorrectly-classified dog breed:")
        count = 0
        for file_name in results_dic.keys():
            if sum(results_dic[file_name][3:]) == 2 and results_dic[file_name][2] == 0:
                print("{} is a(n) {}, but is classified as a(n) {}.".format(file_name,results_dic[file_name][0],results_dic[file_name][1]))
                count += 1
        if not count: # count==0
            print("None")
    
    # print interesting results that are human-readable
    print_interesting_results(results_stats_dic)

def print_interesting_results(results_stats_dic):
    """
    Prints interesting results to me, that the grader doesn't appreciate
    including:
        N Correctly-Classified Dog Breeds,
        N Correctly-Classified ANY Breeds,
        The Confusion Matrix, and
        other statistics for the classifier in human-readable language.
    """
    
    
    ### start
    print("\n\n")
    print("----------------------------------------------------------------------------------")
    print("---- Below are the things I personally find interesting and want to print out ----")
    print("-------  because I find key names inadequate in fully describing the stats -------")
    print("----------------------------------------------------------------------------------")
    
    # print N Correctly-Classified Dog Breeds and N Correctly-Classified ANY Breeds
    print("{:>35}: {:3d}".format('N Correctly-Classified Dog Breeds', results_stats_dic['n_correct_breed'])) # E
    print("{:>35}: {:3d}".format('N Correctly-Classified ANY Breeds', results_stats_dic['n_match'])) # Y
    
    # print confusion matrix
    labels=['dogs','NON-dogs']
    print_dog_matrix(results_stats_dic, labels)
    
    # print other interesting stats in human-readable language
    
    ## pct_match # ROW 1 in Submission-feedback # COL 4 in Results Table < Final Results < Course Project
    print_human_message(stat_name = None, n_den = results_stats_dic["n_images"], n_num=results_stats_dic["n_match"], judgment_pct=results_stats_dic["pct_match"], 
                        judgment = "the breed", key_dict = "pct_match")

    ## pct_correct_breed # ROW 3 in Submission-feedback # COL 3 in Results Table < Final Results < Course Project
    print_human_message(stat_name = None, n_den = results_stats_dic["n_dogs_img"], n_num=results_stats_dic["n_correct_breed"], judgment_pct=results_stats_dic["pct_correct_breed"],
                        judgment = "the breed", pool_actual = "dog", key_dict = "pct_correct_breed")
    
    ## pct_correct_dogs # ROW 2 in Submission-feedback # COL 2 in Results Table < Final Results < Course Project
    #name = "Recall(    dog)=Sensitivity(    dog)"
    name = "{:^20} = {:^20}".format("{:12}({:3} {:3})".format("Recall","","dog"),"{:12}({:3} {:3})".format("Sensitivity","","dog"))
    print_human_message(stat_name = name, 
                        n_den = results_stats_dic["n_dogs_img"], n_num = results_stats_dic["n_correct_dogs"], judgment_pct = results_stats_dic["pct_correct_dogs"], 
                        pool_actual = "dog", key_dict = "pct_correct_dogs")

    ## pct_correct_notdogs # ROW 4 in Submission-feedback # COL 1 in Results Table < Final Results < Course Project
    #name = "Recall(not dog)=Specifity (    dog)"
    name = "{:^20} = {:^20}".format("{:12}({:3} {:3})".format("Recall","not","dog"),"{:12}({:3} {:3})".format("Specifity","","dog"))
    print_human_message(stat_name = name, 
                        n_den = results_stats_dic['n_notdogs_img'], n_num = results_stats_dic["n_correct_notdogs"], judgment_pct = results_stats_dic["pct_correct_notdogs"], 
                        pool_actual="NON-dog", key_dict = "pct_correct_notdogs")
    
    ## Precision (dog)
    #name = "Precision(dog)"
    name = "{:^20}   {:^20}".format("{:12} {:3} {:3} ".format("","",""),"{:12}({:3} {:3})".format("Precision","","dog"))
    a = results_stats_dic["n_correct_dogs"]
    b = (results_stats_dic["n_correct_dogs"]+results_stats_dic["n_notdogs_img"]-results_stats_dic["n_correct_notdogs"])
    print_human_message(stat_name = name, n_den=b, n_num=a, judgment_pct=pct(a,b), 
                        pool_classifier = "dog")
    
    ## Overall Accuracy(dog/NON-dog)
    #name = "Overall Accuracy( dog/NON-dog )"
    name = "{:^8}   {:>34}".format("","{:10}({:12})".format("Accuracy","dog/NON-dog"))
    a = (results_stats_dic["n_correct_dogs"]+results_stats_dic["n_correct_notdogs"])
    b = results_stats_dic["n_images"]
    print_human_message(stat_name = name, n_den=b, n_num=a, judgment_pct=pct(a,b))   
    
    return None
    
def print_dog_matrix(results_stats_dic, labels=["dogs","NON-dogs"]):
    """
    Prints the confusion matrix of the 2 categories described by labels.
    Columns are the actual, labeled as "actual <labels[0]>" & "actual <labels[1]>";
    Rows are the classified, labeled as "classified <labels[0]>" & "classified <labels[1]>".
    
    Parameters:
      results_stats_dic:    Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      labels:   List that contains 2 categories.
                Default value: ["dogs","NON-dogs"]
    Returns:
           None - simply printing results.    
    """
    print("\n\n")
    print("*** Confusion Matrix ( {} vs. {} ) ***".format(labels[0],labels[1]))
    labels_actual = ["actual "+label for label in labels]
    labels_classified = ["classified "+label for label in labels]
    data = [[results_stats_dic["n_correct_dogs"], results_stats_dic["n_notdogs_img"]-results_stats_dic["n_correct_notdogs"]],
            [results_stats_dic["n_dogs_img"]-results_stats_dic["n_correct_dogs"], results_stats_dic["n_correct_notdogs"]]]
    format_row = "{:>22}" * (len(labels_actual) + 1)
    print(format_row.format("", *labels_actual))
    for classified, row in zip(labels_classified, data):
        print(format_row.format(classified, *row))
    print("\n\n")
    return None

def print_human_message(stat_name = None, n_den = None, n_num = None, judgment = "dog/NON-dog", judgment_pct = None, pool_classifier = None, pool_actual = None, key_dict = None):
    """
    prints percentage stats in human-readable language, in the following format:
    {:>46}  {:28}{:24}, {:40}:{:>8}  {:20}
    [<stat_name>                        :] out of all <n_den> <pool_actual> imgs [classified as <pool_classifier>], <n_num> correct in judging <judgment>    :  <judgment_pct>%    [<key_dict>]
    
    stat_name = None    :   str, the name of the stat being printed
    n_den = None        :   int, the denominator in the pct presented
    n_num = None        :   int, the numerator in the pct presented
    judgment_pct = None :   float, the percentage presented
    judgment = "dog/NON-dog"    :   str, the judgment type
    pool_classifier = None  :str, the denominator classification category, if applicable
    pool_actual = None  :   str, the denominator actual category, if application
    key_dict = None     :   str, the corresponding key in dic results_stats_dic, if application
    
    Returns:
           None - simply printing results.    
           
    e.g. calling this program with the following lines
    print_human_message(stat_name = "Recall(not dog)=Specifity (    dog)", 
                        n_den = 10, n_num = 9, judgment_pct = 90.0, 
                        pool_actual = "NON-dog", key_dict = "pct_correct_notdogs")
    prints the following message on the screen
    
    Recall(not dog)=Specifity (    dog):  out of all    10 NON-dog  imgs                        ,     9 correct in judging dog/NON-dog    :  90.00%pct_correct_notdogs
    """
    fmt1 = "{:>46}"
    fmt2 = "  {:28}"
    fmt3 = "{:24}, "
    fmt4 = "{:40}"
    fmt5 = ":{:>8}"
    fmt6 = "  {:20}"
    fmt = fmt1+fmt2+fmt3+fmt4+fmt5+fmt6
    
    # txt1: "<stat_name>:"
    if stat_name:
        stat_name += ":"
    else:
        stat_name=""
    txt1 = stat_name
    
    # txt2: "out of all <n_den> [<pool_actual>] imgs"
    if pool_actual:
        txt2 = "out of all {:5d} {:8} imgs".format(n_den, pool_actual)
    else:
        txt2 = "out of all {:5d} {:8} imgs".format(n_den, "")
    
    # txt3: "[classified as <pool_classifier>],"
    if pool_classifier:
        txt3 = " classified as {}".format(pool_classifier)
    else:        
        txt3 = ""
    
    # txt4: "<n_num> correct in judging <judgment>"
    txt4 = "{:5d} correct in judging {}".format(n_num, judgment)
    
    # txt5: "<jdgement_pct>%"
    txt5 = "{:6.2f}%".format(judgment_pct)   
    
    # txt6: "<key_dict>"
    if key_dict:
        txt6 = key_dict
        print(fmt.format(txt1,txt2,txt3,txt4,txt5,txt6))
    else:        
        print(fmt.format(txt1,txt2,txt3,txt4,txt5,""))
        
    return None
          