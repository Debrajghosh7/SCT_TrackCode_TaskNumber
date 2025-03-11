#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <matplotlibcpp.h>
namespace plt = matplotlibcpp;

const char* file_path = "C:\\Users\\HP\\OneDrive\\Desktop\\US_Accidents_March23.csv";

typedef struct {
    char Start_Time[20];
    int Severity;
    char Weather_Condition[50];
    double Latitude;
    double Longitude;
} Accident;

Accident* load_data(const char* file_path, int* num_records) {
    FILE* file = fopen(file_path, "r");
    if (!file) {
        perror("Unable to open file");
        exit(EXIT_FAILURE);
    }

    char line[256];
    *num_records = 0;
    Accident* accidents = malloc(sizeof(Accident) * 10000); // Assuming a maximum of 10,000 records

    while (fgets(line, sizeof(line), file)) {
        if (*num_records >= 10000) break; // Prevent overflow
        sscanf(line, "%[^,],%d,%[^,],%lf,%lf", accidents[*num_records].Start_Time, &accidents[*num_records].Severity,
               accidents[*num_records].Weather_Condition, &accidents[*num_records].Latitude, &accidents[*num_records].Longitude);
        (*num_records)++;
    }
    fclose(file);
    return accidents;
}

void analyze_data(Accident* accidents, int num_records) {
    int accidents_by_hour[24] = {0};
    int accidents_by_day[7] = {0};
    int accidents_by_weather[10] = {0}; // Assuming 10 different weather conditions
    int severity_distribution[5] = {0}; // Assuming severity levels from 1 to 5

    for (int i = 0; i < num_records; i++) {
        struct tm tm;
        strptime(accidents[i].Start_Time, "%Y-%m-%d %H:%M:%S", &tm);
        int hour = tm.tm_hour;
        int day = tm.tm_wday;

        accidents_by_hour[hour]++;
        accidents_by_day[day]++;
        accidents_by_weather[accidents[i].Weather_Condition[0] - 'A']++; // Simplified for demonstration
        severity_distribution[accidents[i].Severity - 1]++;
    }

    plt::figure_size(1200, 600);
    plt::bar(std::vector<int>(accidents_by_hour, accidents_by_hour + 24));
    plt::title("Accident Frequency by Hour of the Day");
    plt::xlabel("Hour of the Day");
    plt::ylabel("Number of Accidents");
    plt::show();

    plt::figure_size(1000, 500);
    plt::bar(std::vector<int>(accidents_by_day, accidents_by_day + 7));
    plt::title("Accidents by Day of the Week");
    plt::xlabel("Day of the Week");
    plt::ylabel("Number of Accidents");
    plt::show();

    plt::figure_size(1400, 600);
    plt::bar(std::vector<int>(accidents_by_weather, accidents_by_weather + 10));
    plt::title("Top 10 Weather Conditions Leading to Accidents");
    plt::xlabel("Weather Condition");
    plt::ylabel("Number of Accidents");
    plt::show();

    plt::figure_size(800, 500);
    plt::bar(std::vector<int>(severity_distribution, severity_distribution + 5));
    plt::title("Distribution of Accident Severity");
    plt::xlabel("Severity Level");
    plt::ylabel("Number of Accidents");
    plt::show();

    plt::figure_size(1200, 800);
    std::vector<double> latitudes, longitudes;
    for (int i = 0; i < num_records; i++) {
        latitudes.push_back(accidents[i].Latitude);
        longitudes.push_back(accidents[i].Longitude);
    }
    plt::scatter(longitudes, latitudes);
    plt::title("Accident Hotspots");
    plt::xlabel("Longitude");
    plt::ylabel("Latitude");
    plt::show();
}

int main() {
    int num_records;
    Accident* accidents = load_data(file_path, &num_records);
    analyze_data(accidents, num_records);
    free(accidents);
    printf("Analysis complete.\n");
    return 0;
}
