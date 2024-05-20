#include <iostream>
#include <cstdlib>
#include <ctime>

struct CAN_FRAME {
    unsigned long id;
    uint8_t length;
    uint8_t data[8];
};

void simulate_oxygen_sensor_message() {
    CAN_FRAME can_message;
    can_message.id = 0x123;  // Example CAN ID for oxygen sensor
    can_message.length = 8;  // Example data length
    for (int i = 0; i < 8; i++) {
        can_message.data[i] = rand() % 256;  // Random data for simulation
    }

    std::cout << "Simulated CAN Message:" << std::endl;
    std::cout << "ID: 0x" << std::hex << can_message.id << std::dec << " ("
              << can_message.id << ")" << std::endl;
    std::cout << "Length: " << (int)can_message.length << std::endl;
    std::cout << "Data: ";
    for (int i = 0; i < can_message.length; i++) {
        if (i != 0) std::cout << ":";
        std::cout << std::hex << (int)can_message.data[i] << std::dec;
    }
    std::cout << std::endl;
}

int main() {
    srand(time(0));
    for (int i = 0; i < 10; ++i) {
        simulate_oxygen_sensor_message();
    }
    return 0;
}
