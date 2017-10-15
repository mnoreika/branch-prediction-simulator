#include<stdio.h>

int main() {
   int i, j, num = 14, temp = 0;

   int arr[] = {1, 5, 2, 9999, 222, 123, 123123, 4343, 5454, 767, 8787, 4343, 2323, 2323};

   for (i = 1; i < num; i++) {
      temp = arr[i];
      j = i - 1;
      while ((temp < arr[j]) && (j >= 0)) {
         arr[j + 1] = arr[j];
         j = j - 1;
      }
      arr[j + 1] = temp;
   }

   return 0;
}
