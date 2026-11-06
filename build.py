#!/usr/bin/env python3
"""Generates the static Taquionica international site (taquionica.com)."""
import os, html
ROOT = os.environ.get("OUT") or os.path.dirname(os.path.abspath(__file__))
HOME = "index.html" if os.environ.get("PREVIEW") else ""
E = html.escape

EMAIL = "taquionica.oficial@gmail.com"
WA = "https://wa.me/5516993668447?text=" + "Hi%20Taquionica%2C%20I%27d%20like%20to%20discuss%20an%20engineering%20project."
WA_SHOW = "+55 16 99366-8447"
IG = "https://www.instagram.com/taquionica_oficial/"

PROJECTS = {
    "motor":  ("pcb-motor-control.jpg", "Dual motor control board", "Dedicated hardware with a power stage for two motors, protections and control firmware."),
    "iot":    ("pcb-iot-controller.jpg", "Connected controller for remote monitoring", "Integrated Wi-Fi, multiple driver outputs and data sent to a cloud dashboard."),
    "hub":    ("pcb-automation-hub.jpg", "Automation hub for commercial equipment", "Sensor inputs, power relays for 127–220 V, a configuration interface and telemetry."),
    "power":  ("pcb-power-conversion.jpg", "Power conversion and driver board", "DC/DC conversion stage, filtering, protections and a command interface to the inverter."),
    "signal": ("pcb-signal-acquisition.jpg", "Signal acquisition and conditioning board", "Configurable gain and offset, LED status indication and an integration bus."),
    "field":  ("field-implement.jpg", "Embedded automation for a tractor-mounted implement", "Position sensors, hydraulic actuator control, brush speed adjustment and overload protection."),
    "app":    ("app-ble.jpg", "Bluetooth app for equipment setup", "Operating profiles, real-time charts of temperature, voltage and power, and stored history."),
    "dash":   ("dashboard-map.jpg", "Fleet dashboard for installed equipment", "Every connected unit on a map, with live readings and status."),
}

# group, slug, name, one-liner, hero image (key or file), phone?, title, lead, signals, scope, tech, work, faqs
SERVICES = [
 dict(g="build", slug="electronic-product-development", name="Electronic product development",
  short="From an idea or a bench prototype to a product that works in the field.",
  img="pcb-iot-controller.jpg",
  h1="Electronic product development, from first sketch to field-ready unit",
  lead="Hardware, firmware and the software around them, designed by one team. Bring the idea, the requirement or the prototype that never became a product.",
  signals=[("The idea exists, the technical path doesn't", "You know what the product must do, but nobody has turned it into an architecture, a bill of materials and a plan."),
           ("The bench prototype never became a product", "It works on the desk. It is not yet repeatable, protected or ready to be manufactured."),
           ("Suppliers that don't talk to each other", "One company did the board, another the firmware, a third the app, and every problem lands between them."),
           ("It works on the bench and fails in the field", "Noise, unstable power and vibration expose what the prototype never had to handle.")],
  scope=[("Hardware design", "Circuit architecture, component selection, power, protection and interfaces."),
         ("PCB design and review", "Schematic, layout and the files your manufacturer needs."),
         ("Embedded firmware", "Microcontroller code written for the real operating conditions."),
         ("Functional prototype", "A working unit to validate the concept before you commit to production."),
         ("Production readiness", "Documentation, testing and the adjustments that make the product repeatable."),
         ("Apps and connectivity", "When the product needs a phone app, a dashboard or the cloud, the same team builds it.")],
  tech=["ESP32 and PIC microcontrollers", "Wi-Fi", "Bluetooth Low Energy", "MQTT", "Modbus", "CAN"],
  work=["iot", "motor", "app"],
  faqs=[("Can you start from an idea with no drawings?", "Yes. The first step is understanding what the product must do and under which conditions. From there we propose an architecture and a scope before any development starts."),
        ("Who manufactures the boards?", "We assemble the boards for the products we develop. If you already have a manufacturer, we deliver production files for them.")]),
 dict(g="build", slug="hardware-design", name="Hardware design",
  short="Circuits, sensors, power and communication designed for the job the equipment has to do.",
  img="pcb-power-conversion.jpg",
  h1="Hardware designed for the equipment you actually run",
  lead="When off-the-shelf boards don't fit, or your current hardware has reached its limit, we design the electronics around your process: sensing, power, protection and communication.",
  signals=[("Off-the-shelf boards don't fit", "The available modules almost work, and the workarounds cost more than a proper design."),
           ("Your current hardware hit its limit", "New features, new sensors or new communication won't fit the board you have."),
           ("You need technology of your own", "Depending on a third-party controller limits what you can sell and support."),
           ("A previous project stalled halfway", "Someone started the design and left. You need a team that can pick it up.")],
  scope=[("Circuit architecture", "Block diagram, power budget and the choice of microcontroller and components."),
         ("Sensors and interfaces", "Analog and digital inputs, signal conditioning, drivers and actuators."),
         ("Power and protection", "Supply stages, filtering and protection for the environment the board will live in."),
         ("Communication", "Wired and wireless links chosen for the site, not for the catalogue."),
         ("Prototyping and validation", "Bench and field tests before the design is frozen."),
         ("Evolution of existing products", "Redesigns that keep what works and fix what doesn't.")],
  tech=["Power electronics", "DC/DC conversion", "Signal conditioning", "Motor drivers", "Relays and contactors"],
  work=["power", "signal", "motor"],
  faqs=[("Can you work on top of a board we already have?", "Yes. We review the existing design, explain what limits it and propose either a revision or a new design."),
        ("Do you also write the firmware?", "Yes. Hardware and firmware are designed together, which avoids most of the problems that appear when they are done separately.")]),
 dict(g="build", slug="pcb-design", name="PCB design and layout",
  short="Schematics, layout and manufacturing files, or a review of the board that keeps failing.",
  img="pcb-signal-acquisition.jpg",
  h1="PCB design and layout, ready for your manufacturer",
  lead="Engineering design for printed circuit boards: schematic, component choice, layout and routing, with noise and protection handled from the start. Fabrication stays with your supplier.",
  signals=[("A board that fails in the field", "Random resets, corrupted readings or burnt components usually trace back to layout and protection."),
           ("A schematic without a layout", "The circuit is defined, but nobody has turned it into a board that can be built."),
           ("A design that is hard to manufacture", "Assembly problems, rework and low yield push the cost of every unit up."),
           ("Noise and interference", "Switching stages and long cables couple into sensitive signals.")],
  scope=[("Schematic and components", "A clear schematic and parts chosen for availability, cost and the operating environment."),
         ("Layout and routing", "Placement and routing that respect power, signal integrity and assembly."),
         ("Noise reduction and protection", "Grounding, filtering and protection planned from the first draft."),
         ("Manufacturing files", "Gerbers, drill files, bill of materials and assembly drawings ready to send.")],
  tech=["Power and signal layout", "Noise reduction", "Protection circuits", "Manufacturing files"],
  work=["signal", "power", "motor"],
  faqs=[("Do you fabricate the PCBs?", "For this service we deliver the design and the production files; manufacturing stays with your supplier."),
        ("Can you review a board designed by someone else?", "Yes. We review the schematic and layout, point out the likely causes of failure and the order in which to fix them.")]),
 dict(g="build", slug="firmware-development", name="Firmware development",
  short="Embedded code for microcontrollers, written, fixed or extended by the people who design the hardware.",
  img="pcb-motor-control.jpg",
  h1="Firmware development for equipment that can't stop",
  lead="New firmware, or the firmware you already have made stable and extensible. Written by the same team that designs the hardware, so the code and the circuit agree with each other.",
  signals=[("The equipment locks up or resets", "Blocking code, missing watchdogs and poor error handling show up as random failures."),
           ("Every change breaks something else", "The code grew without structure and nobody wants to touch it."),
           ("Updates require a technician on site", "Without remote updates, every fix means travel."),
           ("Communication drops", "Wi-Fi, Bluetooth or industrial buses lose messages under real conditions.")],
  scope=[("New firmware", "Architecture, drivers, control logic and communication for a new product."),
         ("Rescue and refactoring", "Stabilising existing code and making it maintainable."),
         ("Communication protocols", "Wi-Fi, Bluetooth, MQTT, Modbus, CAN and serial links."),
         ("Remote updates", "Firmware delivered to installed units without a technician on site."),
         ("Sensors, displays and actuators", "Reading, filtering and controlling the hardware around the microcontroller."),
         ("Testing", "Validation on the bench and on the real equipment.")],
  tech=["ESP32", "PIC", "MQTT", "Modbus RTU/TCP", "CAN", "BLE", "Over-the-air updates"],
  work=["motor", "hub", "field"],
  faqs=[("Can you work on firmware written by another company?", "Yes. We start with an analysis of the code and the hardware, then propose fixing it or rewriting the parts that can't be saved."),
        ("Can firmware be updated remotely?", "Yes. We have kept a fleet of more than 45 connected units updated remotely for over six years.")]),
 dict(g="connect", slug="iot-remote-monitoring", name="IoT and remote monitoring",
  short="Know what your equipment is doing without sending someone to look.",
  img="app-mqtt.jpg", phone=True,
  h1="Remote monitoring for equipment spread across many sites",
  lead="We connect your equipment to the internet so it reports readings, raises alerts and accepts commands from anywhere. Board, firmware, cloud, dashboard and app, built as one system.",
  signals=[("You only learn about a failure on site", "The problem becomes visible when someone arrives, usually after it has grown."),
           ("Technicians travel just to check", "Routine verification consumes time and fuel that a reading could replace."),
           ("No data from the field", "Without history, every decision about maintenance or design is a guess."),
           ("Too many units to follow", "Tracking dozens of machines by phone calls and spreadsheets doesn't scale.")],
  scope=[("Hardware and boards", "Connected controllers designed for your equipment, or added to it."),
         ("Firmware", "Reliable reading, buffering and reconnection when the network fails."),
         ("Communication", "Wi-Fi, Bluetooth, cellular or industrial buses, chosen for the site."),
         ("Cloud and database", "Storage and history for every unit in the fleet."),
         ("Dashboard", "A clear view of status, readings and alerts across all units."),
         ("Mobile app", "Configuration and control from the operator's phone.")],
  tech=["MQTT", "Wi-Fi", "BLE", "Modbus", "Cloud dashboards", "Android"],
  work=["dash", "iot", "app"],
  faqs=[("Can you connect equipment we already have in the field?", "Often, yes. We look at the existing electronics and decide whether to read them directly or add a connected controller."),
        ("How long has this kind of system been running?", "Our connected fleet has more than 45 units running continuously for over six years, updated remotely.")]),
 dict(g="connect", slug="machine-data-collection", name="Machine data collection",
  short="Production, downtime and status read from the machine and delivered to a dashboard.",
  img="dashboard-map.jpg",
  h1="Machine data collection, from the sensor to the dashboard",
  lead="Your production line generates data every minute. We read it from the machine, move it reliably and turn it into indicators that managers can act on.",
  signals=[("Reports arrive late", "The shop floor knows what happened yesterday; management finds out next week."),
           ("Data lives in notebooks and spreadsheets", "Manual records are incomplete and impossible to compare."),
           ("Downtime has no explanation", "Stops are noticed, but their causes and duration are not recorded."),
           ("Old machines with no outputs", "The equipment works well but was never designed to share data.")],
  scope=[("Reading the machine", "Sensors, PLC registers or existing signals, depending on the equipment."),
         ("Gateway and communication", "Reliable transport from the machine to the server, with buffering for network gaps."),
         ("Production indicators", "Output, downtime and availability calculated from real data."),
         ("Dashboard and alerts", "The indicators your team needs, with alerts when something leaves its range.")],
  tech=["Modbus RTU/TCP", "MQTT", "Industrial sensors", "Gateways", "Dashboards"],
  work=["dash", "iot", "hub"],
  faqs=[("Do we need to replace our machines?", "No. In most cases we read the machine as it is, adding sensors or a gateway where needed."),
        ("Where does the data go?", "To a server and dashboard defined with you at the start of the project.")]),
 dict(g="connect", slug="apps-and-dashboards", name="Apps and dashboards for equipment",
  short="Phone apps and web dashboards to configure, follow and control your equipment.",
  img="app-ble.jpg", phone=True,
  h1="Apps and dashboards that put the equipment in the operator's hand",
  lead="The equipment is good; the way people use it is not. We build the app and the dashboard together with the firmware, so configuration, live readings and alerts just work.",
  signals=[("Setup needs a laptop and a cable", "Every configuration change requires a technician and special software."),
           ("Operators can't see what's happening", "Readings exist inside the equipment but never reach a screen."),
           ("No overview of the installed base", "Each unit is managed alone, with no shared view."),
           ("The app and the firmware disagree", "Different suppliers mean features that never quite match.")],
  scope=[("On-site configuration", "Bluetooth apps for setup and operating profiles."),
         ("Real-time readings", "Live charts of temperature, voltage, current, power and more."),
         ("Control and alerts", "Commands and notifications when values leave their limits."),
         ("Fleet dashboard", "A web view of every installed unit, on a map or in a list.")],
  tech=["Android", "Bluetooth Low Energy", "MQTT", "Web dashboards", "Maps"],
  work=["app", "dash", "iot"],
  faqs=[("Do you build only the app if we already have the hardware?", "Yes, as long as we can access the equipment's communication protocol. If the firmware needs changes, we can do that too."),
        ("Which platforms do you support?", "Our apps run on Android, and dashboards run in any modern browser.")]),
 dict(g="connect", slug="industrial-software-and-hmi", name="Industrial software and HMI",
  short="Operator interfaces, integration with legacy machines and custom industrial software.",
  img="dashboard-map.jpg",
  h1="Industrial software and HMI that understand what's on the other end of the cable",
  lead="We are not a software house. We build interfaces, integrations and back-ends for equipment, which means we understand the signals, the protocols and the failures behind each screen.",
  signals=[("Equipment that doesn't talk to anything", "Machines, apps and platforms that stay isolated from each other."),
           ("Off-the-shelf software doesn't fit", "Generic systems ask your process to change instead of adapting to it."),
           ("Legacy machines nobody wants to replace", "They still produce, but have no way to share data or accept commands."),
           ("Operators walk to the machine to read a value", "Information that should be on a screen still depends on a visit.")],
  scope=[("HMI and operator interfaces", "Screens designed for the people who run the process."),
         ("Integration with legacy equipment", "Reading and controlling existing machines through their available signals."),
         ("Data history", "Storage and history for analysis and audits."),
         ("Back-end and cloud", "The services that connect equipment, apps and users.")],
  tech=["Modbus", "MQTT", "Serial protocols", "Databases", "Android", "Web"],
  work=["dash", "app", "hub"],
  faqs=[("Can you integrate with machines from different manufacturers?", "Yes, as long as they expose a signal or protocol we can read. We map that at the start of the project."),
        ("Do you maintain the software after delivery?", "We plan delivery and evolution together, so improvements and new features can follow.")]),
 dict(g="improve", slug="industrial-automation", name="Industrial automation",
  short="Control systems for motors, pumps, sensors and processes, designed for the scale of your operation.",
  img="pcb-automation-hub.jpg",
  h1="Industrial automation built for the scale of your operation",
  lead="Automating one machine is different from automating a whole operation. We design the control, the sensing and the records so the solution can be repeated across lines and sites.",
  signals=[("Manual processes slow the line", "Repetitive tasks consume people, time and consistency."),
           ("Inconsistent control between machines", "Each unit was automated differently and none of them can be compared."),
           ("Fragmented suppliers", "A different vendor for every system, and nobody responsible for the whole."),
           ("No operational record", "What happened in the field isn't stored anywhere.")],
  scope=[("Custom automation", "Control logic designed around the real process."),
         ("Sensors and actuators", "Motors, pumps, relays, valves and sensors integrated into one system."),
         ("Telemetry and records", "Operational history for maintenance and management."),
         ("Hardware and firmware in-house", "The controller is designed by the same team that writes its code.")],
  tech=["Motor control", "Relays and contactors", "Industrial sensors", "Modbus", "Telemetry"],
  work=["hub", "field", "motor"],
  faqs=[("Do you work with existing PLCs?", "When a PLC is the right tool, we integrate with it. When a dedicated controller fits better, we design one."),
        ("Can the solution be replicated across sites?", "That is a design goal from the start: standard hardware, firmware and records that scale.")]),
 dict(g="improve", slug="machine-retrofit", name="Machine retrofit",
  short="Keep the mechanics, replace the electronics and control, and connect the machine to the plant.",
  img="pcb-motor-control.jpg",
  h1="Machine retrofit: the mechanics still work, the electronics don't have to stay old",
  lead="When a machine is mechanically sound but its controls are obsolete, unavailable or unreliable, we redesign the electronics and control around it, and connect it to the rest of the plant.",
  signals=[("Spare parts are no longer available", "A failed board can stop the machine for weeks."),
           ("Unexplained stops", "The control fails intermittently and nobody can find the cause."),
           ("No way to collect data", "The machine produces, but can't report what it is doing."),
           ("A replacement costs far more than the problem", "Buying a new machine to fix a control issue doesn't add up.")],
  scope=[("Survey on the machine", "We study the machine, its signals and the way it is operated."),
         ("New control electronics", "Boards designed for the machine, with protections for its environment."),
         ("Control firmware", "Logic rewritten and documented, so it can be maintained."),
         ("Connection to the plant", "Data and alerts sent to your dashboard or system.")],
  tech=["Motor drivers", "Power stages", "Industrial sensors", "Modbus", "Telemetry"],
  work=["motor", "hub", "field"],
  faqs=[("Is retrofit always worth it?", "Not always. The survey tells us whether the mechanics justify new electronics, and we say so if they don't."),
        ("Do you repair the existing board?", "No. We don't do repair or maintenance work; we redesign the control.")]),
 dict(g="improve", slug="technical-diagnostics", name="Technical diagnostics",
  short="An engineering review of hardware, firmware and communication when equipment fails in the field.",
  img="pcb-power-conversion.jpg",
  h1="Technical diagnostics for equipment that fails where you can't see it",
  lead="Electrical noise, poor power, unstable communication, blocking firmware and layout problems can undermine a whole product. We find the likely causes and the order in which to fix them.",
  signals=[("The failure only happens at the customer's site", "It never shows on the bench, so nobody can reproduce it."),
           ("Rounds of trial and error", "Parts are swapped and code is patched without a clear diagnosis."),
           ("Random resets and corrupted readings", "Symptoms that usually point to power, noise or firmware."),
           ("You need an independent opinion", "Before investing in a redesign, you want to know what is really wrong.")],
  scope=[("Hardware review", "Circuit, components, power and protection."),
         ("Firmware analysis", "Blocking code, error handling and timing."),
         ("Communication assessment", "Wired and wireless links under real conditions."),
         ("PCB review and report", "Layout, grounding and noise, with a written report of causes and next steps.")],
  tech=["Noise and EMI", "Power integrity", "Firmware review", "Protocol analysis"],
  work=["power", "motor", "signal"],
  faqs=[("How is a diagnostic priced?", "After understanding the equipment and the failure, we send an estimate in hours before any work starts."),
        ("What do we receive at the end?", "The probable causes, the order in which to address them and the recommended path to fix and evolve the product.")]),
 dict(g="improve", slug="engineering-outsourcing", name="Electronic engineering outsourcing",
  short="A technical arm for your team: the engineering the scope requires, without an idle payroll.",
  img="pcb-signal-acquisition.jpg",
  h1="Electronic engineering outsourcing, sized to the project",
  lead="Your project is waiting in line for an engineer you never had time to hire. We work as your technical arm, with one accountable lead and specialists who join as each stage requires.",
  signals=[("Projects waiting for engineering capacity", "The roadmap is ready, the team is not."),
           ("A skill your team doesn't have", "Power electronics, layout or embedded firmware are needed for one project."),
           ("Hiring doesn't make sense", "A full-time team would sit idle between projects."),
           ("You need one accountable partner", "Not a pool of freelancers to coordinate.")],
  scope=[("Technical diagnosis", "We understand the requirement and the current state of the project."),
         ("Architecture and fixed scope", "Scope, timeline and price agreed before development starts."),
         ("Development with a team sized to scope", "Specialists join as each stage of the project requires."),
         ("Delivery and documentation", "Files, code and documentation your team can own.")],
  tech=["Hardware", "PCB", "Firmware", "Apps", "Integration"],
  work=["motor", "power", "app"],
  faqs=[("Who do we talk to during the project?", "One person: our project manager and technical lead, from diagnosis to delivery."),
        ("Who owns the results?", "Ownership of designs and code is defined in the contract before work begins.")]),
 dict(g="improve", slug="field-embedded-electronics", name="Embedded electronics for field equipment",
  short="Control and telemetry for agricultural machines and implements that face vibration, dust and unstable power.",
  img="field-implement.jpg",
  h1="Embedded electronics for machines that work in the field",
  lead="On the bench, voltage is stable and nobody touches the board. In the field the implement vibrates all day, power swings with the engine and dust gets everywhere. We design for that.",
  signals=[("Machines that only report after they stop", "Without information, problems are found when the work has already been lost."),
           ("Electronics that don't survive the field", "Boards designed for clean environments fail under vibration and dust."),
           ("Manual adjustments during operation", "Operators compensate by hand for what the control should handle."),
           ("No record of the work done", "What the machine did, where and for how long is not stored.")],
  scope=[("Embedded control", "Position sensing, hydraulic actuators, speed control and protections."),
         ("Field-grade electronics", "Power, protection and enclosures for vibration, dust and humidity."),
         ("Telemetry and alerts", "Data from the machine to a dashboard the operation follows."),
         ("Remote updates", "Firmware updated across the fleet without a visit.")],
  tech=["Agricultural machinery", "Hydraulic control", "Position sensors", "Telemetry", "Over-the-air updates"],
  work=["field", "dash", "motor"],
  faqs=[("Do you work with implement manufacturers?", "Yes. We can develop the electronics as part of your product or as an upgrade to machines already in use."),
        ("How do you choose the communication link?", "By the conditions on site: coverage, distance and how often data must arrive.")]),
]
GROUPS = [
 ("build", "Build", "Design the electronics and the code inside your product."),
 ("connect", "Connect", "Get data out of the equipment and into the hands of the people who decide."),
 ("improve", "Improve", "Automate, modernise and fix the equipment you already run."),
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

ARROW = '<svg class="go" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def menu_html(depth):
    sp = "" if depth else "services/"
    out = ""
    for gk, gname, gdesc in GROUPS:
        out += f'          <div class="menu-col"><p class="menu-h">{gname}</p><ul>'
        for s in SERVICES:
            if s["g"] == gk:
                out += f'<li><a href="{sp}{s["slug"]}.html">{E(s["name"])}</a></li>'
        out += "</ul></div>\n"
    return out.rstrip("\n")

def head(title, desc, path, depth):
    p = "../" * depth
    MENU = menu_html(depth)
    canon = "https://taquionica.com/" + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://taquionica.com/assets/img/og.jpg">
<link rel="icon" type="image/png" href="{p}assets/img/symbol-orange.png">
<link rel="alternate" hreflang="pt-BR" href="https://taquionica.com.br/">
<link rel="preload" href="{p}assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css?v=1">
<script src="{p}assets/site.js?v=1" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{p}{HOME or ('' if p else './')}" aria-label="Taquionica home"><img src="{p}assets/img/logo-h-orange.png" alt="Taquionica" width="220" height="40"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      <div class="nav-svc">
        <button class="nav-svc-btn" aria-expanded="false" aria-controls="svc-menu">Services</button>
        <div class="svc-menu" id="svc-menu">
{MENU}
        </div>
      </div>
      <a href="{p}{HOME}#work">Work</a>
      <a href="{p}{HOME}#process">Process</a>
      <a href="{p}{HOME}#purpose">Mission</a>
      <a href="{p}{HOME}#about">About</a>
      <a class="btn btn-primary" href="#contact">Get a quote</a>
    </nav>
  </div>
</header>
<main id="main">
"""

def foot(depth):
    p = "../" * depth
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <img src="{p}assets/img/logo-h-white.png" alt="Taquionica" width="155" height="30">
    <p>Electronic engineering since 2016. Ribeirão Preto, São Paulo, Brazil.</p>
    <div class="foot-links">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{WA}" rel="noopener">WhatsApp</a>
      <a href="{IG}" rel="noopener">Instagram</a>
      <a href="https://taquionica.com.br/" hreflang="pt-BR">Português</a>
    </div>
  </div>
</footer>
</body>
</html>
"""

def contact_section(depth, preselect=""):
    opts = "".join(f'<option{" selected" if s["name"]==preselect else ""}>{E(s["name"])}</option>' for s in SERVICES)
    return f"""
<section class="on-dark contact" id="contact">
  <div class="wrap contact-grid">
    <div>
      <h2>Tell us what the equipment needs to do</h2>
      <p class="lead">Fill in the form and it opens a WhatsApp conversation with our project manager, with your details already written. We reply within one business day and sign an NDA before the technical call if you need one.</p>
      <ul class="channels">
        <li><a href="{WA}" rel="noopener"><span class="k">WhatsApp</span><span class="v">{WA_SHOW}</span></a></li>
        <li><a href="mailto:{EMAIL}?subject=Project%20inquiry"><span class="k">Email</span><span class="v">{EMAIL}</span></a></li>
      </ul>
      <div class="fineprint">
        <ul>
          <li>We work with companies only.</li>
          <li>Scope, timeline and price are agreed before development starts.</li>
          <li>We don't take academic, hobby, repair or maintenance work.</li>
          <li>Business hours in Brazil (UTC−3). Calls scheduled across time zones.</li>
        </ul>
      </div>
    </div>
    <form class="wa-form" novalidate data-wa="5516993668447">
      <div class="f-row">
        <label class="f">Name<input name="name" autocomplete="name" required></label>
        <label class="f">Company<input name="company" autocomplete="organization" required></label>
      </div>
      <div class="f-row">
        <label class="f">Work email<input name="email" type="email" autocomplete="email" required></label>
        <label class="f">Country<input name="country" autocomplete="country-name" required></label>
      </div>
      <label class="f">Service<select name="service" required><option value="">Choose a service</option>{opts}<option>Not sure yet</option></select></label>
      <label class="f">What does the project need?<textarea name="message" rows="5" required placeholder="The equipment, what it must do, and where you are today: idea, prototype or product in the field."></textarea></label>
      <p class="f-error" role="alert" hidden>Fill in every field so we can answer with something useful.</p>
      <button class="btn btn-primary f-submit" type="submit">Send on WhatsApp</button>
      <p class="f-note">Opens WhatsApp with your message ready to send. Nothing is stored on this site.</p>
      <p class="f-fallback" hidden>If WhatsApp didn't open, <a class="f-link" href="#" rel="noopener">tap here to open it</a>.</p>
    </form>
  </div>
</section>
"""

def work_fig(key, cls, depth, tall=False):
    img, t, d = PROJECTS[key]
    p = "../" * depth
    return f"""<figure class="work {cls}{' tall' if tall else ''}"><div class="ph"><img src="{p}assets/img/{img}" alt="{E(t)}" loading="lazy"></div><figcaption><strong>{E(t)}</strong><span>{E(d)}</span></figcaption></figure>"""

def home():
    out = head("Taquionica — Electronic engineering: hardware, firmware and IoT",
               "Taquionica designs electronic products end to end: hardware, PCB, firmware, IoT, apps and dashboards. One engineering team from Brazil, working with companies worldwide.",
               "", 0)
    out += """
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <h1>From the circuit board to the screen in your hand.</h1>
        <p class="lead">Taquionica designs the electronics, firmware and software that make equipment work, and keeps working, in the field. One team for every layer, so nothing gets lost between suppliers.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="#contact">Get a quote</a>
          <a class="btn btn-ghost" href="#services">Explore services</a>
        </div>
        <p class="hero-note">Engineering in Brazil for companies worldwide. NDA before the first technical call.</p>
      </div>
      <figure class="hero-visual">
        <div class="sheet">
          <img src="assets/img/pcb-iot-cutout.png" alt="Connected controller board designed by Taquionica, with an ESP32 module, output drivers and sensor inputs" width="655" height="486">
          <svg class="callouts" viewBox="0 0 100 80" preserveAspectRatio="none" aria-hidden="true">
            <path d="M38.8 23.8 V6.4"/><circle cx="38.8" cy="23.8" r=".9"/>
            <path d="M46.2 35.3 H81"/><circle cx="46.2" cy="35.3" r=".9"/>
            <path d="M24 52.3 V73.6"/><circle cx="24" cy="52.3" r=".9"/>
          </svg>
          <span class="co" style="left:40.5%;top:3.5%">Output drivers</span>
          <span class="co co-r" style="left:82%;top:40.5%">ESP32<br>Wi‑Fi and Bluetooth</span>
          <span class="co" style="left:25.7%;top:89%">5 V supply</span>
        </div>
        <figcaption>A connected controller we designed, programmed and linked to a cloud dashboard and phone app.</figcaption>
      </figure>
    </div>
    <dl class="facts">
      <div><dt>Since 2001</dt><dd>our technical lead has designed electronic equipment</dd></div>
      <div><dt>45+ units online</dt><dd>running continuously for more than six years</dd></div>
      <div><dt>Updated remotely</dt><dd>new firmware delivered to the fleet without a site visit</dd></div>
    </dl>
  </div>
</section>

<section class="on-dark stack" id="layers">
  <div class="wrap">
    <div class="sec-head">
      <h2>One engineering team for every layer of the system</h2>
      <p class="lead">Most equipment problems live between layers: the firmware that doesn't match the board, the app that doesn't match the firmware. We design the whole chain, so those gaps don't exist.</p>
    </div>
    <ol class="stack-list">
"""
    layers = [
        ("Hardware", "Circuits, sensors, power stages and the printed circuit board, designed for the conditions the equipment will face.", ["hardware-design", "pcb-design"]),
        ("Firmware", "Code on the microcontroller that reads, controls, protects and communicates, and can be updated remotely.", ["firmware-development", "electronic-product-development"]),
        ("Connectivity", "Wi-Fi, Bluetooth, MQTT, Modbus and CAN, chosen for the site rather than the catalogue.", ["iot-remote-monitoring", "machine-data-collection"]),
        ("Software", "Dashboards, phone apps and operator interfaces that turn readings into decisions and commands.", ["apps-and-dashboards", "industrial-software-and-hmi"]),
    ]
    for name, txt, links in layers:
        lk = "".join(f'<a href="services/{s}.html">{E(BY_SLUG[s]["name"])}</a>' for s in links)
        out += f'      <li class="stack-item"><span class="pad" aria-hidden="true"></span><h3>{name}</h3><p>{E(txt)}</p><div class="links">{lk}</div></li>\n'
    out += """    </ol>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="sec-head">
      <h2>Services</h2>
      <p class="lead">Take the whole project to us, or only the part your team is missing. Each service has its own page with what's included and the questions companies usually ask.</p>
    </div>
    <div class="svc-groups">
"""
    for gk, gname, gdesc in GROUPS:
        out += f'      <div class="svc-group"><header><h3>{gname}</h3><p>{E(gdesc)}</p></header><ul class="svc-list">\n'
        for s in SERVICES:
            if s["g"] == gk:
                out += f'        <li><a href="services/{s["slug"]}.html"><span class="n">{E(s["name"])}</span><span class="d">{E(s["short"])}</span>{ARROW}</a></li>\n'
        out += "      </ul></div>\n"
    out += """    </div>
  </div>
</section>

<section class="on-white" id="work">
  <div class="wrap">
    <div class="sec-head">
      <h2>Equipment in operation</h2>
      <p class="lead">A selection of boards, apps and systems designed by Taquionica. Client names stay private: every project is delivered under confidentiality.</p>
    </div>
    <div class="work-grid">
"""
    out += work_fig("iot", "w-7", 0) + work_fig("power", "w-5", 0)
    out += work_fig("motor", "w-4", 0) + work_fig("signal", "w-4", 0) + work_fig("hub", "w-4", 0)
    out += work_fig("dash", "w-8", 0) + work_fig("field", "w-4", 0)
    out += """
    </div>
  </div>
</section>

<section class="purpose" id="purpose">
  <div class="wrap purpose-grid">
    <div>
      <p class="purpose-k">Our mission</p>
      <p class="purpose-quote">Use technology to make the world a better place for everyone to live in.</p>
    </div>
    <div class="purpose-copy">
      <p class="lead">Not as an abstract intention. Every monitored unit is food that doesn't spoil, medicine that keeps its effectiveness, energy that isn't wasted and a technician trip that no longer has to happen.</p>
      <p class="muted">Our goal is to give companies technology of their own: equipment that is connected, processes that run without manual work, and data that turns into decisions. Well-made engineering reduces waste, gives people their time back and protects whoever is running the operation. That is the result we measure every project by.</p>
      <ul class="aims">
        <li><strong>Connect equipment</strong><span>so problems are seen before they become losses</span></li>
        <li><strong>Automate tasks</strong><span>so people stop doing what a machine should do</span></li>
        <li><strong>Turn data into decisions</strong><span>so every choice rests on what really happens in the field</span></li>
      </ul>
    </div>
  </div>
</section>

<section id="process">
  <div class="wrap">
    <div class="sec-head">
      <h2>How a project runs</h2>
      <p class="lead">You know the scope, the timeline and the price before any development starts. After that, you follow each stage with the same person.</p>
    </div>
    <ol class="steps">
      <li><h3>Understanding</h3><p>You describe the idea, the equipment or the problem. We sign an NDA first if you need one.</p></li>
      <li><h3>Diagnosis</h3><p>We assess requirements, risks, constraints and technical options.</p></li>
      <li><h3>Planning</h3><p>Architecture, scope, stages, deliverables and price, agreed in writing.</p></li>
      <li><h3>Development</h3><p>Hardware, firmware, software and communication, built and integrated by one team.</p></li>
      <li><h3>Testing</h3><p>Operation, communication and stability validated on the bench and on the real equipment.</p></li>
      <li><h3>Delivery and evolution</h3><p>Files, code and documentation delivered, with a plan for improvements and new features.</p></li>
    </ol>
  </div>
</section>

<section class="on-dark" id="about">
  <div class="wrap about-grid">
    <figure class="portrait" style="margin:0"><img src="assets/img/nell.jpg" alt="Nell, project manager and technical lead at Taquionica" width="719" height="1077" loading="lazy"><figcaption>Nell, project manager and technical lead</figcaption></figure>
    <div class="about-copy">
      <h2>Engineering shaped by sectors where mistakes are expensive</h2>
      <p class="lead">Our technical lead started designing electronic equipment in 2001. The first twelve years were spent on regulated medical devices, under the requirements of ANVISA, Brazil's health regulator. We no longer take on medical projects, but the discipline stayed.</p>
      <p class="muted">Next came vehicle monitoring for revenue control on toll roads, where a measurement error becomes lost revenue the same day. Taquionica was founded in 2016 to bring that standard to every project: protection and margin are never an afterthought.</p>
      <p class="muted">You talk to one person from diagnosis to delivery. Specialists in power electronics, PCB layout, firmware, apps and integration join as each stage requires, so the team grows and shrinks with the project.</p>
      <dl class="place">
        <div><dt>Based in</dt><dd>Ribeirão Preto, São Paulo, Brazil</dd></div>
        <div><dt>Working with</dt><dd>Companies in Brazil and abroad, remotely</dd></div>
      </dl>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap faq-grid">
    <h2>Questions companies ask before hiring us</h2>
    <div class="faq">
"""
    faqs = [
        ("Do you work with companies outside Brazil?", "Yes. Engineering is done in Brazil; design files, source code and documentation are delivered digitally, and calls are scheduled across time zones."),
        ("Can you develop only one part of the project?", "Yes. We can take the whole system or only the layer your team is missing: hardware, PCB, firmware, app or integration."),
        ("Can you improve equipment that already exists?", "Yes. Many projects start with a product that works but needs new features, better reliability or connectivity."),
        ("How is confidential information protected?", "We sign an NDA before the technical conversation when needed, and we never publish client names or project details."),
        ("How is the price defined?", "Every project is sized to the real problem, so the price comes out of the technical conversation, not a table. You receive scope, timeline and price before development starts."),
        ("Do you manufacture boards?", "We assemble the boards for the products we develop. We don't assemble boards designed by others; for PCB design work, we deliver production files for your manufacturer."),
    ]
    for q, a in faqs:
        out += f"      <details><summary>{E(q)}</summary><p>{E(a)}</p></details>\n"
    out += """    </div>
  </div>
</section>
"""
    out += contact_section(0)
    out += foot(0)
    return out

def service_page(s):
    d = 1
    p = "../"
    title = f"{s['name']} — Taquionica"
    out = head(title, s["lead"], f"services/{s['slug']}", d)
    phone = s.get("phone")
    imgcls = "ph phone" if phone else "ph"
    out += f"""
<section class="svc-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../{HOME}">Home</a> / <a href="../{HOME}#services">Services</a> / {E(s['name'])}</p>
    <div class="svc-hero-grid">
      <div>
        <h1>{E(s['h1'])}</h1>
        <p class="lead">{E(s['lead'])}</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="#contact">Get a quote</a>
          <a class="btn btn-ghost" href="#scope">What's included</a>
        </div>
      </div>
      <div class="{imgcls}"><img src="{p}assets/img/{s['img']}" alt="" ></div>
    </div>
  </div>
</section>

<section class="on-dark">
  <div class="wrap">
    <div class="sec-head"><h2>When companies call us</h2><p class="lead">If one of these sounds familiar, this is the service to start with.</p></div>
    <ul class="signals">
"""
    for t, x in s["signals"]:
        out += f"      <li><strong>{E(t)}</strong><span>{E(x)}</span></li>\n"
    out += f"""    </ul>
  </div>
</section>

<section id="scope">
  <div class="wrap">
    <div class="sec-head"><h2>What's included</h2><p class="lead">Take all of it or only the part you need. The scope is agreed in writing before development starts.</p></div>
    <div class="scope">
"""
    for t, x in s["scope"]:
        out += f"      <div><h3>{E(t)}</h3><p>{E(x)}</p></div>\n"
    out += "    </div>\n    <ul class=\"tech\" aria-label=\"Technologies\">" + "".join(f"<li>{E(t)}</li>" for t in s["tech"]) + "</ul>\n  </div>\n</section>\n"
    out += """
<section class="proof">
  <div class="wrap">
    <dl class="facts">
      <div><dt>One accountable lead</dt><dd>you talk to the same person from diagnosis to delivery</dd></div>
      <div><dt>45+ units online</dt><dd>running continuously for more than six years, updated remotely</dd></div>
      <div><dt>Fixed scope first</dt><dd>scope, timeline and price agreed in writing before development</dd></div>
    </dl>
  </div>
</section>
"""
    out += """
<section class="on-white">
  <div class="wrap">
    <div class="sec-head"><h2>Related work</h2><p class="lead">Equipment designed by Taquionica and in operation today. Client names are kept private.</p></div>
    <div class="work-grid">
"""
    out += "".join(work_fig(k, "w-4", d) for k in s["work"])
    out += """
    </div>
  </div>
</section>

<section>
  <div class="wrap faq-grid">
    <div>
      <h2>Common questions</h2>
      <div class="related">
"""
    others = [o for o in SERVICES if o["g"] == s["g"] and o["slug"] != s["slug"]][:3]
    out += "".join(f'<a href="{o["slug"]}.html">{E(o["name"])}</a>' for o in others)
    out += """
      </div>
    </div>
    <div class="faq">
"""
    common = [("How do we start?", "Send a short description by email or WhatsApp. We reply within one business day, sign an NDA if needed and schedule the technical conversation."),
              ("Do you work with companies outside Brazil?", "Yes. Files, code and documentation are delivered digitally, and calls are scheduled across time zones.")]
    for q, a in s["faqs"] + common:
        out += f"      <details><summary>{E(q)}</summary><p>{E(a)}</p></details>\n"
    out += """    </div>
  </div>
</section>
"""
    out += contact_section(d, s["name"])
    out += foot(d)
    return out

def write(rel, txt):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(txt)

write("index.html", home())
for s in SERVICES:
    write(f"services/{s['slug']}.html", service_page(s))

notfound = head("Page not found — Taquionica", "Page not found", "404", 0).replace('href="./"', 'href="/"')
notfound = notfound.replace('assets/', '/assets/').replace('href="#', 'href="/#')
notfound += """<section><div class="wrap"><h1>This page doesn't exist.</h1><p class="lead" style="margin:24px 0 32px">The link may be old or mistyped.</p><a class="btn btn-primary" href="/">Go to the home page</a></div></section>"""
notfound += foot(0).replace('assets/', '/assets/')
write("404.html", notfound)

urls = ["https://taquionica.com/"] + [f"https://taquionica.com/services/{s['slug']}" for s in SERVICES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: https://taquionica.com/sitemap.xml\n")
write("CNAME", "taquionica.com\n")
print("ok", len(SERVICES), "services")
