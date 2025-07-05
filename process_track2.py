import pandas as pd
from functools import reduce

def read_and_process_csv(file_path, score_name):
    """
    Reads a CSV file, processes it, and returns a DataFrame.
    - Reads the first two columns.
    - Cleans the video name by taking the part after the last '/'.
    - Renames columns to 'video_name' and a specific score name.
    """
    try:
        df = pd.read_csv(file_path, usecols=[0, 1])
        col1_name = df.columns[0]
        col2_name = df.columns[1]

        df.rename(columns={
            col1_name: 'video_name',
            col2_name: score_name
        }, inplace=True)

        df['video_name'] = df['video_name'].astype(str).str.split('/').str[-1]
        return df
    except FileNotFoundError:
        print(f"Warning: File not found at {file_path}. It will be skipped.")
        return None
    except Exception as e:
        print(f"Warning: Could not process {file_path}. Error: {e}. It will be skipped.")
        return None

def main():
    """
    Main function to calculate weighted scores from multiple CSV files.
    """
    # There were some missing commas in the file list from the prompt.
    # I have corrected the file paths based on the calculation logic.
    file_definitions = {
        'trad_8b': 'AIGVQA_8B/weights/eval/mos1_1/mos1.csv',
        'trad_26b': 'AIGVQA_26B/weights/eval/mos1_2/mos1.csv',
        'align_26b_1': 'AIGVQA_26B/weights/eval/mos2_1/mos2.csv',
        'align_26b_2': 'AIGVQA_26B/weights/eval/mos2_2/mos2.csv',
        'aesth_8b': 'AIGVQA_8B/weights/eval/mos3_1/mos3.csv',
        'aesth_9b': 'AIGVQA_9B/weights/eval/mos3_2/mos3.csv', # Using mos3_2 from the file list
        'temp_8b': 'AIGVQA_8B/weights/eval/mos4_1/mos4.csv',
        'temp_26b_1': 'AIGVQA_26B/weights/eval/mos4_2/mos4.csv',
        'temp_26b_2': 'AIGVQA_26B/weights/eval/mos4_3/mos4.csv',
    }

    dataframes = []
    for name, path in file_definitions.items():
        df = read_and_process_csv(path, name)
        if df is not None:
            dataframes.append(df)

    if not dataframes:
        print("Error: No valid data could be read. Exiting.")
        return

    # Merge all dataframes on 'video_name' using an outer join
    merged_df = reduce(lambda left, right: pd.merge(left, right, on='video_name', how='outer'), dataframes)

    # Fill missing scores with 0 so they don't affect the weighted sum
    merged_df.fillna(0, inplace=True)

    # Calculate the weighted scores
    # Handling cases where a file might have been skipped by checking column existence
    merged_df['Traditional_MOS'] = (merged_df.get('trad_8b', 0) * 0.6) + \
                                 (merged_df.get('trad_26b', 0) * 0.4)

    merged_df['Alignment_MOS'] = (merged_df.get('align_26b_1', 0) * 0.5) + \
                               (merged_df.get('align_26b_2', 0) * 0.5)

    merged_df['Aesthetic_MOS'] = (merged_df.get('aesth_9b', 0) * 0.5) + \
                               (merged_df.get('aesth_8b', 0) * 0.5)

    merged_df['Temporal_MOS'] = (merged_df.get('temp_8b', 0) * 0.4) + \
                              (merged_df.get('temp_26b_1', 0) * 0.2) + \
                              (merged_df.get('temp_26b_2', 0) * 0.4)

    # Select final columns and sort
    output_columns = ['video_name', 'Traditional_MOS', 'Alignment_MOS', 'Aesthetic_MOS', 'Temporal_MOS']
    final_df = merged_df[output_columns].sort_values(by='video_name').reset_index(drop=True)

    # Save to Excel
    output_filename = 'prediction2.xlsx'
    try:
        final_df.to_excel(output_filename, index=False)
        print(f"Successfully created {output_filename}")
    except Exception as e:
        print(f"Error: Could not save the Excel file. {e}")


if __name__ == "__main__":
    main()
