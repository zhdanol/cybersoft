from check import storage_buckets

def test_safe_buckets():
    config = {"storage_buckets": [
        {"name": "backups", "public": False, "encrypted": True}
    ]}
    assert storage_buckets(config) == []
   
def test_pub_buckets():
    config = {"storage_buckets": [
        {"name": "public-logs", "public": True, "encrypted": False}
    ]}
    
    assert len(storage_buckets(config)) == 2

def test_no_encrypt():
    config = {"storage_buckets": [
        {"name": "user-uploads", "public": True, "encrypted": False}
    ]}
    
    assert len(storage_buckets(config)) == 2
