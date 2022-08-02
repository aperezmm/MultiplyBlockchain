from brownie import Stackies, accounts, config

def deploy():

    account = accounts.add(config["wallets"]["from_key"])
    print(f"Vamos a usar la siguiente cuenta : {account}")

    stackies = Stackies.deploy(
        "0.01 ether",
        20,
        10,
        {"from": account },       
        publish_source = True
    )

    print(stackies)

def main():
    deploy()