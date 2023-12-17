
This function creates a multi-level dictionary for DICOM meta data (named dicom_data) in a directory (named dicom_dir).
The top level has the last component of dicom_dir, which is the first level subfolder, as a key.
For each subforled it will store study data within this dic, along with another dicitonary for series data, within this study dictionary.
For series dictionary the data corresponding for series number will be stored.
We also have another private_info dictionary within subfodler dictionary.

- dicom_validation: If you set dicom_validation=True, it will validate the file in the loop for being an dicom file. This is super important although it makes code slower.
Becaouse, sometimes some dicom files have no extension, and also reading other files may cause error in the loop.

- folder_list_name_indicomdir: #In your dicom_dir you can include list of folders name that you want to read. It will not read other folders. Kepp in mind that this will look into subfolders in the main folder, and not the subfolders of subfolders :)

- store_as_json_dir: if you want to store your ditionary as json, give your desired json direcotry

- store_as_excel_dir: if you want to store your ditionary as excel, give your desired excel direcotry

For using this function, the best practice is to place each folder containing one dicom study in subfolder, under the dicom_dir. 
However, you can change finding unique dicom studies, even placed next to each other beacouse I definied the study_unique=f'{first_subfolder}_{study_id}_{study_date}'.
If you want your code to be faster you can chane the study_unique to study_unique=first_subfolder. It makes your code 15% faster, sometimes at the cost of incurrect retrival.

20231215 by Amir Safavi :)