from pathlib import Path


dir_path = Path (".")



for child in dir_path.iterdir():

    if child.is_file():
            
        extension = child.suffix.lower()
        if extension:
            label = extension[1:].upper()
                
        else:
            label = "NO-EXT"
        
        try:
            
            label_path = dir_path / label
            label_path.mkdir(parents=True, exist_ok=True)
            label_file_path = label_path / child.name
            
            if child.parent == label_path:
                continue
            
            child.rename(label_file_path)
                
            print (child.name, "------>", "file", "label ====>> ",label)
            
        except TypeError as T:
            print ("an error has been raised |||", type(T).__name__)
            
            
    else:
        print (child.name, "------>", "dir")
