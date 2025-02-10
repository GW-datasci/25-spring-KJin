#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(777) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """777""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Comparing GPTs against Traditional Transformer Algorithms in Detecting Misinformation""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            In 2022, researchers created a multimodal dataset of 21 million tweets called MuMiN to see how well a graph-based
            algorithm detected misinformation spread against a text-based one, the former obtaining an F1-score of 61.45% and
            the latter obtaining 52.80%. In this project, we wish to have ChatGPT-4o and DeepSeek analyze a subset of the same
            data to analyze how they compare to the algorithms in the original study in detecting misinformation.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
          Data Source: https://github.com/MuMiN-dataset/mumin-build
          Study: https://dl.acm.org/doi/10.1145/3477495.3531744
          In the dataset, there is text (tweet message), images, dates, integers, and floats (percentages). The data was
          collected by Dan S. Nielsen and Ryan McConville, researchers from the Department of Engineering Mathematics in
          the University of Bristol. Additionally, their article was peer-reviewed, making the data quite reliable barring
          any glaring issues upon closer inspection of the dataset.
  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Impact":
            """
            This project will provide insight into the advantages and disadvantages of both traditional machine learning
            models and generative AI models like ChatGPT-4 or DeepSeek for detecting misinformation. By evaluating their performance,
            scalability, and contextual understanding, this study will help justify the use of one model over the other in
            different contexts. The insights gained from this comparison will guide organizations in selecting appropriate
            algorithms to combat misinformation effectively and may also inform government policies on addressing the
            spread of false information in digital spaces.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            Data Preparation
            - Choose which subsets of data to extract from the dataset and one copy
            - Process the copied data subset exactly as is in the article
            Reproducing Baseline Results
            - Use MuMiN to analyze the measurements of the copied subset data
            Experiments with ChatGPT-4o and DeepSeek
            - Craft multiple prompts that range in specificity before inputting them
            Analyze comparison
            - Calculate the significance of the differences in scoring, including query time.
            Compiling Results and Insights
            - Use RStudio to create data visualizations of results.
            Writing Final Report
            Poster and Final Presentation
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            (1 Week) Data Preparation
            (1 Week) Reproducing Baseline Results
            (2 Weeks) Experiments with ChatGPT-4o
            (2 Weeks) Analyze comparison
            (3 Weeks) Compiling Results and Insights
            (3 Weeks) Writing Final Report
            (2 Weeks) Poster and Final Presentation
            """,
       # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            GPTs may analyze even a relatively small sample of data extremely slowly compared to traditional ML algorithms.
            - May need to eliminate photos from the data, likely decreasing accuracy.
            Analyzing 21 million posts will take too much memory.
            - Sample X posts completely at random to best ensure no sampling error.
            GPTs may misinterpret instructions.
            - Extreme articulation in the prompt regarding what measurements it needs to make, using the original article as a guide (though specificity regarding everything else can vary).
            GPT’s memories of past chat logs may affect results.
            - Create a free trial account, and copy and delete the previous cat log whenever beginning a new series of prompts.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Kevin Jin",
        "Proposed by email": "kjin23@gwu.edu",
        "instructor": "Sushovan Majhi",
        "instructor_email": "s.majhi@gwu.edu",
        "github_repo": "https://github.com/GW-datasci/25-spring-KJin",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
