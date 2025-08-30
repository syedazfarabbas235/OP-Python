from word_frequency_counter import WordFrequencyCounter

def main():
    try:
        
        tracker=WordFrequencyCounter("zoro law zoro garp aizen zoro")
        tracker.process_text()
        print (tracker)
    except Exception as e:
        print(f"error:{e}")    

if __name__ == "__main__":
    main()
