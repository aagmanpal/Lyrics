#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <chrono>

void printLirik() {
    std::vector<std::tuple<std::string, int, int>> lirik = {
        {"Dengar larakuu.......", 4300, 70},
        {"Suara hati ini memanggil namamu", 2000, 120},
        {"Kar'na separuh aku", 3200, 120}, {"Menyentuh laramu", 4300, 120},
        {"", 1100, 0},  
        {"Semua lukamu t'lah menjadi lirihku", 2000, 120},
        {"Kar'na separuh aku", 3500, 120},
        {"Dirimu", 1300, 150},
        
        {"\n- Noah Separuh Aku -", 1100, 0}, 
        
    };

    // Cetak lirik dengan huruf muncul satu per satu dengan delay yang berbeda
    for (const auto& baris : lirik) {
        const std::string& teks = std::get<0>(baris);
        int delayBaris = std::get<1>(baris);
        int delayHuruf = std::get<2>(baris);

        for (char c : teks) {
            std::cout << c << std::flush;
            std::this_thread::sleep_for(std::chrono::milliseconds(delayHuruf)); // Delay per huruf
        }
        std::cout << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(delayBaris)); // Delay setelah baris selesai
        
    }
}

int main() {
    // Panggil fungsi untuk mencetak lirik
    printLirik();
    return 0;
}
