//stack implementation all in o(1) including getMin

class MinStack {
private:
    std::stack<long> s;
    long min;
public:
    MinStack() {}
    
    void push(int val) {
        if (s.empty()){
            s.push(0);
            min = val;
        }
        else{
            s.push(val-min);
            if (val<min){
                min = val;
            }
        }
    }
    
    void pop() {
        long last = s.top();
        s.pop();
        if (last<0){
            min -= last;
        }
    }
    
    int top() {
        long top = s.top();
        if (top<0){
            return min;
        }
        return top+min;
    }
    
    int getMin() {
        return min;
    }
};
