#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int x) : data(x), next(NULL) {}
};

bool isPalindrome(Node* head) {
    vector<int> v;
    while (head) {
        v.push_back(head->data);
        head = head->next;
    }
    return equal(v.begin(), v.end(), v.rbegin());
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(2);
    head->next->next->next = new Node(1);

    cout << (isPalindrome(head) ? "Palindrome" : "Not Palindrome");

    return 0;
}