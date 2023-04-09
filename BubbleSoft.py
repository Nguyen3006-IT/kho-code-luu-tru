#include <iostream>
using namespace std;

// tạo hàm con để hoán đổi giá trị bé và lớn
void swap(int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
// hàm thuật toán BBS thực thi
void bubbleSort(int a[], int n){
    int i, j;
    for (i = 0; i < n - 1; i++){
        for (j = 0; j < n - i - 1; j++)
            if (a[j] > a[j + 1]){
                swap(a[j], a[j + 1]);   
            }
    }
}
// hàm xuất kết quả
void xuat(int a[], int n){
    for (int i = 0 ; i < n; i++ ) 
    cout << a[i] << "  ";
}
// hàm để khai báo (hàm chủ yếu)
int main(){ 
    int a[1000]; //kích thước tối đa là 1000
    int n;  // kích thước giá trị nguyên dương
    cout << "nhap n: ";
    cin >> n ;  // nhập kích thước đề yêu cầu
    for (int i = 0 ; i < n; i++ ) {
        cout << "a[" << i + 1 << "] = ";
        cin >> a[i];
    }
    // khai báo hàm con 
    bubbleSort(a, n);
    xuat (a, n);
    
    return 0;
}
