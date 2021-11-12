import pandas as pd


if __name__ == '__main__':
    columns = ["Subject", "Start Date",	"Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]

    with open('timetable_12-11-2021.csv', 'r') as f:
        header = False
        schedule = pd.DataFrame(columns=columns)

        for line in f:
            if header:
                header = False
                continue

            if line == '\n':
                header = True
            else:
                woofs = [*map(lambda woof: woof.strip(" \n").replace("\"", ""), line.split(";"))]
                if len(woofs) != 1:
                    schedule = schedule.append({
                        "Subject": woofs[0],
                        "Start Date": woofs[3],
                        "Start Time": woofs[4],
                        "End Date": woofs[6],
                        "End Time": woofs[7],
                        "All Day Event": False,
                        "Description": f"{woofs[9]} by {woofs[10]}.\nnote: {woofs[-1]}",
                        "Location": woofs[11],
                        "Private": True
                    }, ignore_index=True)
                else:
                    header = True
        print(schedule)
    schedule.to_csv('./schedule.csv', index=False)
