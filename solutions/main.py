import time
from multiprocessing import Pool
from library import download_video, read_video_urls

if __name__ == "__main__":
    # Load the URLs from our data folder
    videos = read_video_urls("data/video_urls.csv")
    urls = [v["url"] for v in videos]

    # Phase 06: Parallel Execution
    start_p = time.perf_counter()
    
    with Pool() as pool:
        pool.map(download_video, urls)
        
    end_p = time.perf_counter()
    parallel_time = round(end_p - start_p, 2)
    
    print(f"Parallel execution: {parallel_time}")

    # Comparison logic using our known serial baseline
    serial_time = 1.89 
    improvement = round(((serial_time - parallel_time) / serial_time) * 100, 2)

    # Final report logging
    with open("reports/sequential_report.md", "a") as f:
        f.write(f"\n## Parallel execution\nTotal time: {parallel_time} seconds\n")
        f.write(f"\n## Comparison\nSpeed improvement: {improvement}%\n")