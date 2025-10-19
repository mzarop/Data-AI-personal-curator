import yaml
from scr.collector import collect_save_data

def main():
    # Load YAML config
    with open("settings/config.yaml",'r') as file:
        config = yaml.safe_load(file)

    # Run the collector with the loaded config
    collect_save_data(config)



if __name__ == "__main__":
    main()


