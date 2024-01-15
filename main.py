import sys
from LoginAndExtractData import extractProntoInformationIntoJson
from ExtractDataFromJson import extractDataFromJsonAndWriteIntoExcel
from tqdm import tqdm

def readCommandLine():
    if len(sys.argv) != 2:
        print("Error: Incorrect Command-line arguments!")
        sys.exit(1)

    feature_ID = sys.argv[1]

    return feature_ID

def main():
    feature_ID = readCommandLine()
    with tqdm(total=3, desc="Main Progress", unit="step") as pbar:
        pbar.set_postfix({"Current Step": "Extracting Pronto Information"})
        pr_numbers, api = extractProntoInformationIntoJson(feature_ID)
        pbar.update(1)
        pbar.set_postfix({"Current Step": "Extracting and Writing to Excel"})
        extractDataFromJsonAndWriteIntoExcel(feature_ID, pr_numbers)
        pbar.update(1)
        pbar.set_postfix({"Current Step": "Finished"})
        api.logout
        pbar.update(1)

if __name__ == "__main__":
    main()