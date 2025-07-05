 import pandas as pd
import os

def process_and_merge_csvs(file_paths):
    """
    Reads multiple CSV files, processes them, merges them, and calculates the average MOS.

    Args:
        file_paths (list): A list of paths to the CSV files.

    Returns:
        pandas.DataFrame: A DataFrame with the first column (cleaned) and the averaged second column,
                          sorted by the first column.
    """
    all_data = []
    for i, file_path in enumerate(file_paths):
        try:
            # Read first two columns, assume a header row exists
            df = pd.read_csv(file_path, usecols=[0, 1])

            # Get column names by position
            col1_name = df.columns[0]
            col2_name = df.columns[1]

            # Clean the first column: take content after the last '/' if it exists
            df[col1_name] = df[col1_name].astype(str).str.split('/').str[-1]

            # Rename columns for consistent merging
            df = df.rename(columns={
                col1_name: 'video_name',
                col2_name: f'Overall_MOS_{i+1}'
            })
            all_data.append(df)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return None
        except (KeyError, IndexError):
            print(f"Error: Could not process columns in {file_path}. It might not have at least two columns.")
            return None

    if not all_data:
        return None

    # Merge all dataframes on 'video_name'
    merged_df = all_data[0]
    for i in range(1, len(all_data)):
        merged_df = pd.merge(merged_df, all_data[i], on='video_name', how='outer')

    # Calculate the average of the 'Overall_MOS' columns
    mos_cols = [f'Overall_MOS_{i+1}' for i in range(len(file_paths))]
    merged_df['Overall_MOS'] = merged_df[mos_cols].mean(axis=1)

    # Prepare final dataframe and sort by 'video_name'
    result_df = merged_df[['video_name', 'Overall_MOS']].sort_values(by='video_name').reset_index(drop=True)

    return result_df

def main():
    """
    Main function to execute the script.
    """
    file_paths = [
        'AIGVQA_8B/weights/eval/mos0_1/mos0.csv',
        'AIGVQA_8B/weights/eval/mos0_2/mos0.csv',
        'AIGVQA_26B/weights/eval/mos0_3/mos0.csv',
        'AIGVQA_26B/weights/eval/mos0_4/mos0.csv'
    ]

    result_df = process_and_merge_csvs(file_paths)

    if result_df is not None:
        output_filename = 'prediction.xlsx'
        # Save to Excel
        result_df.to_excel(output_filename, index=False)
        print(f"Successfully created {output_filename}")

if __name__ == "__main__":
    main()
