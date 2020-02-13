import pandas as pd

emp_df = pd.DataFrame(
    [
        ["E1", "BALWINDER KATOCH", "FIN"],
        ["E2", "MAMTA KATOCH", "HR"],
        ["E3", "ARYAN KATOCH", "ENG"],
        ["E4", "AADI KATOCH", "HR"],
    ],
    columns=["EMP_ID", "NAME", "DEPT"],
)

dept_df = pd.DataFrame(
    [["FIN", "Finance"], ["ENG", "Engineering"], ["HR", "Human Resource"]],
    columns=["DEPT_ID", "NAME"],
)
dept_df.set_index("DEPT_ID", inplace=True)
emp_df.set_index("EMP_ID", inplace=True)

eg = emp_df.groupby("DEPT")
eg = eg.size()
eg = eg.sort_values(ascending=False)

dic = dict(eg)

for x in dic:
    print(f"{x} = {dic[x]}")

