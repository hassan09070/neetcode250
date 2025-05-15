class MyHashSet {
private:
    vector<bool> hashSet;
public:
    MyHashSet() {
        hashSet.resize(1000001, false); // initially all values are false
    }
    
    void add(int key) {
        hashSet[key] = true;
    }
    
    void remove(int key) {
        hashSet[key] = false;
    }
    
    bool contains(int key) {
        return hashSet[key];
    }
};
