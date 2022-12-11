from datetime import datetime
import logging

def logout(input, output_type: int):
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", format="%(levelname)s %(message)s")
    dt = datetime.now().strftime('%d/%m/%Y')
    
    if output_type == 0: # output_type = dict (settings, languages...)
        _output = logging.info(f"[TIME: {dt}][DICTIONARY: {input}]")
        
    elif output_type == 1: # output_type = text (title, artist...)
        _output = logging.info(f"[TIME: {dt}][DATA: {input}]")
        
    elif output_type == 2: # output_type = update success
        _output = logging.info(f"[TIME: {dt}][TEXT: OSError ex]")
    
    else:
        _output = logging.info(f"[TIME: {dt}][TEXT: UNKNOWN OUTPUT_TYPE]")