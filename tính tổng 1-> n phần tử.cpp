#include <stdio.h>
#include <iostream>
using namespace std;
// mảng khai báo in ra màn hình 
int main(){
    int n, a, i; 
    a = 0;
    cout << "nhap n" << ": "; 
    cin >> n ; 
    for(i = 0; i <= n; i++){ // kết quả của vòng lập for này là i = {0, 1, 2, ..., n}
        a = a + i; // có thể viết tắt a += i
    }
    // xuất ra màn hình là 1 + 2 + ... + n-1 + n = tổng 
    cout << n - n+1 << " + " << n - n+2 << " +" << "...+ " << n-1 << " + " << n << " = " << a;
} 
