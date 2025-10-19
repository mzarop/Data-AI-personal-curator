import yaml
from scr.collector import collect_save_data
from scr.simple_users_profils import simple_user

def main():
    # Load YAML config
    with open("settings/config.yaml",'r') as file:
        config = yaml.safe_load(file)

    # Run the collector with the loaded config
    collect_save_data(config)

    #create one user
    user_1 = simple_user(config['users']['name'],config['users']['surname'],config['users']['tags'])
    user_1.display_users()

if __name__ == "__main__":
    main()



