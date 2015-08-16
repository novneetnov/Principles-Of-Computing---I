"""
Cookie Clicker Simulator
"""
#url = http://www.codeskulptor.org/#user39_neLeHGPa7b_15.py

import simpleplot
import math
#import codeskulptor
#codeskulptor.set_timeout(20)


# Used to increase the timeout, if necessary

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies_produced = 0.0
        self._cookies_in_bank = 0.0
        self._current_cps = 1.0
        self._current_time = 0.0
        self._history_lst = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        human_str = "\nCurrent Cookies : " + str(self._cookies_in_bank) + "\n"
        human_str += "current_CPS : " + str(self._current_cps) + "\n"
        human_str += "current time : " + str(self._current_time) + "\n"
        human_str += "total cookies : " + str(self._total_cookies_produced)
        return human_str
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._cookies_in_bank
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history_lst)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies <= self._cookies_in_bank:
            return 0.0
        return math.ceil(float(cookies - self._cookies_in_bank) / self._current_cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._cookies_in_bank += time * self._current_cps
            self._total_cookies_produced += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._cookies_in_bank >= cost:
            self._cookies_in_bank -= cost
            self._current_cps += additional_cps
            self._history_lst.append((self._current_time, item_name, cost, self._total_cookies_produced))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    clicker_state = ClickerState()
    current_time = clicker_state.get_time()
    build_info_clone = build_info.clone()

    while current_time <= duration:
        current_cookies = clicker_state.get_cookies()
        #print "current_cookies ", current_cookies
        current_cps = clicker_state.get_cps()
        #print "current_cps ", current_cps
        current_history_lst = clicker_state.get_history()
        #print "current_history_lst ", current_history_lst
        time_left = duration - current_time
        #print "time_left", time_left
        item_to_buy = strategy(current_cookies, current_cps, current_history_lst, time_left, build_info_clone)
        #print "item_to_buy ", item_to_buy
        if item_to_buy is None:
            clicker_state.wait(time_left)
            break

        item_cost = build_info_clone.get_cost(item_to_buy)
        #print "item_cost ", item_cost
        #required_cookies = item_cost - current_cookies
        #print "required_cookies ", required_cookies
        additional_cps = build_info_clone.get_cps(item_to_buy)
        #print "additional_cps ", additional_cps
        wait_time = clicker_state.time_until(item_cost)
        #print "wait_time", wait_time
        if current_time + wait_time > duration:
            clicker_state.wait(time_left)
            break
        if wait_time == 0:
            clicker_state.buy_item(item_to_buy, item_cost, additional_cps)
            build_info_clone.update_item(item_to_buy)
        else:
            # wait until the time is right and you have enough cookies to buy the item
            clicker_state.wait(wait_time)
            clicker_state.buy_item(item_to_buy, item_cost, additional_cps)
            build_info_clone.update_item(item_to_buy)
            current_time += wait_time

    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    build_items = build_info.build_items()
    min_cost = float("inf")
    min_cost_idx = None
    for idx in range(len(build_items)):
        cost = build_info.get_cost(build_items[idx])
        if cost < min_cost:
            min_cost = cost
            min_cost_idx = idx
    cheapest_item = build_items[min_cost_idx]
    time_req = math.ceil(float(min_cost - cookies) / cps)
    if time_left < time_req:
        return None
    return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    build_items = build_info.build_items()
    max_cost = float("-inf")
    max_cost_idx = None
    for idx in range(len(build_items)):
        cost = build_info.get_cost(build_items[idx])
        time_req = math.ceil(float(cost - cookies) / cps)
        if time_req <= time_left:
            if cost > max_cost:
                max_cost = cost
                max_cost_idx = idx
    if max_cost_idx is None:
        return None
    priciest_item = build_items[max_cost_idx]
    return priciest_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    The item which has the best roi = cps / cost
    """
    build_items = build_info.build_items()
    max_roi = float("-inf")
    max_roi_idx = None
    for idx in range(len(build_items)):
        cost = build_info.get_cost(build_items[idx])
        additional_cps = build_info.get_cps(build_items[idx])
        roi = float(additional_cps) / cost
        time_req = math.ceil(float(cost - cookies) / cps)
        if time_req <= time_left:
            if roi > max_roi:
                max_roi = roi
                max_roi_idx = idx
    if max_roi_idx is None:
        return None
    max_roi_item = build_items[max_roi_idx]
    #print max_roi_item
    return max_roi_item


def strategy_best1(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    The strategy which returns the item which gives the maximum total number of cookies if that item is bought alone.
    """
    build_items = build_info.build_items()
    max_cookies = float("-inf")
    max_factor_item = None
    for item in build_items:
        cookies_till_buy = float(build_info.get_cost(item) - cookies)
        time_req = math.ceil(float(build_info.get_cost(item) - cookies) / cps)
        remainder_cookies_till_end = (cps + build_info.get_cps(item)) * (time_left - time_req)
        if cookies_till_buy > 0:
            total_cookies_produced_item = cookies_till_buy + remainder_cookies_till_end
        else:
            total_cookies_produced_item = remainder_cookies_till_end
        if time_req <= time_left:
            if total_cookies_produced_item > max_cookies:
                max_cookies = total_cookies_produced_item
                max_factor_item = item
    return max_factor_item


def strategy_best2(cookies, cps, history, time_left, build_info):
    """
    The strategy returns first determines the item which gives the best roi.
    If that item can be bought right now, it is returned.
    Else that item is searched, which upon buying will minimize the time required to buy the max roi item.
    Basically it returns the item which shortens the time to get to the best roi item.
    """
    build_items = build_info.build_items()
    best_roi_item = strategy_best(cookies, cps, history, time_left, build_info)
    if best_roi_item is None:
        return None
    time_req_for_best_roi_item = math.ceil(float(build_info.get_cost(best_roi_item) - cookies) / cps)
    best_roi_item_cost = build_info.get_cost(best_roi_item)
    if time_req_for_best_roi_item <= 0:
        return best_roi_item
    less_items = []
    for item in build_items:
        if build_info.get_cost(item) < best_roi_item_cost:
            less_items.append(item)

    min_time = float("inf")
    min_time_item = None
    for item in less_items:
        req_cookies_target = best_roi_item_cost - cookies
        time_req_to_buy_item = math.ceil(float(build_info.get_cost(item) - cookies) / cps)
        time_req_to_reach_target = time_req_to_buy_item + math.ceil(float(req_cookies_target / (cps + build_info.get_cps(item))))
        #print time_req_to_reach_target
        if time_req_to_reach_target < min_time:
            min_time = time_req_to_reach_target
            min_time_item = item
    if min_time < time_req_for_best_roi_item:
        return min_time_item
    else:
        return best_roi_item


def strategy_best3(cookies, cps, history, time_left, build_info):
    """
    The strategy returns the item which gives the best payback time.
    payback time = time required to buy that item + time required to make back the cost paid to buy that item.
    """
    build_items = build_info.build_items()
    best_payback_item = None
    least_payback_time = float("inf")
    for item in build_items:
        time_req_to_purchase_item = math.ceil(float((build_info.get_cost(item) - cookies) / cps))
        time_req_for_payback_post_purchase = math.ceil(float(build_info.get_cost(item)) / build_info.get_cps(item))
        total_payback_time = time_req_for_payback_post_purchase + time_req_to_purchase_item
        if total_payback_time < least_payback_time:
            least_payback_time = total_payback_time
            best_payback_item = item
    #print best_payback_item
    return best_payback_item


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True, [""])


def run():
    """
    Run the simulator.
    """
    run_strategy("Best", SIM_TIME, strategy_best)
    #run_strategy("Strategy_best1", SIM_TIME, strategy_best1)
    run_strategy("Strategy_best2", SIM_TIME, strategy_best2)
    run_strategy("Strategy_best3", SIM_TIME, strategy_best3)
    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    
run()
#print strategy_cheap(2.0, 1.0, [(0.0, None, 0.0, 0.0)], 1.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
#print strategy_expensive(1.0, 3.0, [(0.0, None, 0.0, 0.0)], 17.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
#print simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 15.0, strategy_cursor_broken)