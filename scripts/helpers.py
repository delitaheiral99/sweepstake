from brownie import network, config, accounts

LOCAL_CHAINS = ["development", "ganache-local"]

def is_local_chain():
    return network.show_active() in LOCAL_CHAINS

def get_accounts():
    if is_local_chain():
        return {
            "main_wallet": accounts[0],
            "player1_wallet": accounts[1],
            "player2_wallet": accounts[2],
        }
    else:
        return {
            "main_wallet": accounts.add(config["wallets"]["main_key"]),
            "player1_wallet": config["networks"][network.show_active()]["player1_wallet"],
            "player2_wallet": config["networks"][network.show_active()]["player2_wallet"],
        }
