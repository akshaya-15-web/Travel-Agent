
# Mini Autonomous Travel Agent
# Class Activity 3 - Simple Python Implementation

# ------------------------------------------
# 1. MEMORY DESIGN
# Stores the user's travel preferences.
# ------------------------------------------

memory = {
    "destination": "Goa",
    "days": 3,
    "budget": 10000,
    "transport_preference": "flight",
    "food_preference": "vegetarian"
}


# ------------------------------------------
# 2. TOOL DEFINITIONS
# These tools simulate travel services.
# ------------------------------------------

def check_transport(transport, destination):
    """Check simulated transport availability."""

    print(f"\n[TOOL] Checking {transport} availability to {destination}...")

    # Simulate a flight availability failure
    if transport == "flight":
        return {
            "available": False,
            "message": "No affordable flights available."
        }

    if transport == "train":
        return {
            "available": True,
            "cost": 2500,
            "message": "Train available for Rs. 2500."
        }

    return {
        "available": False,
        "message": "Transport option not available."
    }


def check_weather(destination):
    """Simulate a weather check."""

    print(f"[TOOL] Checking weather in {destination}...")

    return "Sunny weather expected. Sightseeing is suitable."


def create_itinerary(destination, days, food_preference):
    """Create a basic travel itinerary."""

    print("[TOOL] Creating travel itinerary...")

    activities = [
        "Day 1: Explore the beach and local market",
        "Day 2: Visit popular tourist attractions",
        "Day 3: Sightseeing and return journey"
    ]

    print(f"\n--- {days}-Day Itinerary for {destination} ---")

    for activity in activities[:days]:
        print(activity)

    print(f"Food preference: {food_preference}")


def estimate_budget(transport_cost, days):
    """Estimate the total trip cost."""

    hotel_cost = days * 1500
    food_cost = days * 500
    sightseeing_cost = days * 500

    total = (
        transport_cost
        + hotel_cost
        + food_cost
        + sightseeing_cost
    )

    return total


# ------------------------------------------
# 3. AGENT LIFECYCLE
# Goal -> Plan -> Tool -> Observe -> Replan
# -> Reason -> Approval
# ------------------------------------------

def run_travel_agent():

    print("=" * 45)
    print("       MINI AUTONOMOUS TRAVEL AGENT")
    print("=" * 45)

    # GOAL
    destination = memory["destination"]
    days = memory["days"]
    budget = memory["budget"]

    print("\n[GOAL] Plan a trip to", destination)
    print("Duration:", days, "days")
    print("Budget: Rs.", budget)

    # MEMORY
    print("\n[MEMORY] Loading saved preferences...")
    print("Preferred transport:", memory["transport_preference"])
    print("Food preference:", memory["food_preference"])

    # PLANNING
    print("\n[PLANNING] Choosing transport and activities...")

    transport = memory["transport_preference"]

    # TOOL USE
    result = check_transport(transport, destination)

    # OBSERVATION AND FAILURE
    if not result["available"]:

        print("[OBSERVATION] Failure:", result["message"])
        print("[REASONING] The preferred option is unavailable.")
        print("[REPLANNING] Trying an alternative transport...")

        transport = "train"
        result = check_transport(transport, destination)

    # CHECK THE NEW RESULT
    if not result["available"]:
        print("[STOP] No suitable transport was found.")
        return

    print("[OBSERVATION]", result["message"])

    # WEATHER TOOL
    weather = check_weather(destination)
    print("[OBSERVATION]", weather)

    # REASONING AND BUDGET CHECK
    total_cost = estimate_budget(result["cost"], days)

    print("\n[REASONING] Estimated trip cost: Rs.", total_cost)

    if total_cost > budget:
        print("[STOP] The estimated cost exceeds the budget.")
        print("[REPLANNING] Reduce expenses or change the plan.")
        return

    print("[REASONING] The estimated cost is within budget.")

    # CREATE ITINERARY
    create_itinerary(
        destination,
        days,
        memory["food_preference"]
    )

    # FINAL PLAN
    print("\n--- FINAL TRAVEL PLAN ---")
    print("Destination:", destination)
    print("Transport:", transport)
    print("Duration:", days, "days")
    print("Estimated cost: Rs.", total_cost)
    print("Remaining budget: Rs.", budget - total_cost)

    # HUMAN-IN-THE-LOOP SAFETY
    print("\n[HUMAN APPROVAL REQUIRED]")
    print("No booking will happen without your permission.")

    approval = input("Approve the plan? (yes/no): ").strip().lower()

    if approval == "yes":
        print("[ACTION] Plan approved by the user.")
        print("[STATUS] Demo complete. No real booking was made.")
    else:
        print("[ACTION] Booking not approved.")
        print("[STATUS] No booking was made.")

    print("\nTravel agent execution completed.")


# ------------------------------------------
# 4. RUN THE AGENT
# ------------------------------------------

if __name__ == "__main__":
    run_travel_agent()
