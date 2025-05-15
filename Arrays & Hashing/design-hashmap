class MyHashMap {
private:
    vector<int> hashMap;

public:
    MyHashMap() {
        hashMap.resize(1000001, -1);  // Use -1 to denote "not present"
    }
    
    void put(int key, int value) {
        hashMap[key] = value;
    }
    
    int get(int key) {
        return hashMap[key];  // Returns -1 if key was never added or removed
    }
    
    void remove(int key) {
        hashMap[key] = -1;
    }
};
