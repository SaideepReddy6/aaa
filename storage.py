from azure.storage.blob import BlockBlobService, PublicAccess
import os

def run_sample(test):
    block_blob_service = BlockBlobService(account_name='sqlva4djro4jcowsby', account_key='tSejM550BUq4KkdDNmfntJet0eZGu+JrINwf02n1Py/KShnhlvynASekyk4qIxEffyya6v9FT/jQW+CWZX2ryA==')
    container_name ='sdr'
    block_blob_service.create_container(container_name)
    block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)
    local_path=os.path.abspath(os.path.curdir) 
    local_file_name=test  
    full_path_to_file =os.path.join(local_path,'uploads/',test)
    block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
    return('doneee')