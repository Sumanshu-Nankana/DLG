import app

def test_total_route():
    app.app.testing = True
    client = app.app.test_client()
    result = client.get('/total')
    assert result.status_code == 200
    assert result.get_json() == {"total":50000005000000}
        
        
def test_total_route1():
    app.app.testing = True
    client = app.app.test_client()
    result = client.get('/total/3')
    assert result.status_code == 200
    assert result.get_json() == {"total":6}
    
    
if __name__ == "__main__":
    test_total_route()
    test_total_route1()