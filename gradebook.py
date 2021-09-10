from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

roster = pd.read_csv(
    DATA_FOLDER / "roster.cv",
    converters ={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

# load homework file
hw_exam_grades=pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",

)

#https://realpython.com/pandas-project-gradebook/
