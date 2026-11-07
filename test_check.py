from check import storage_buckets

#def test_safe_buckets():
#    config = {"storage_buckets": [
#        {"name": "backups", "public": False, "encrypted": True}
#    ]}
#    assert storage_buckets(config) == []
    

#def test_check_buckets():
#    config = {"storage_buckets": [
#        {"name": "public-logs", "public": True, "encrypted": False}
#    ]}
#    
#    assert len(storage_buckets(config)) == 2
#
#def test_check_buckets():
#    config = {"storage_buckets": [
#        {"name": "public-logs", "public": True, "encrypted": False}
#    ]}
#    
#    assert len(storage_buckets(config)) == 3
    
def test_buck():
    config = {"storage_buckets": [
        {"name": "x", "public": False, "encrypted": False}
    ]}
    
    assert storage_buckets(config) == []