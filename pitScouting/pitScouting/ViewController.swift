//
//  ViewController.swift
//  pitScouting
//
//  Created by Vrishab Madduri on 3/20/18.
//  Copyright © 2018 Vrishab Madduri. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var teamNumber: UITextField!
    @IBOutlet weak var motorInput: UITextField!
    @IBOutlet weak var wheelInput: UITextField!
    @IBOutlet weak var driveInput: UITextField!
    @IBOutlet weak var weightInput: UITextField!
    @IBOutlet weak var autoInput: UITextView!
    @IBOutlet weak var programInput: UITextField!
    @IBOutlet weak var teleInput: UITextView!
    @IBOutlet weak var hangInput: UITextField!
    @IBOutlet weak var assistInput: UITextField!
    @IBOutlet weak var commentInput: UITextField!
    @IBAction func submit(_ sender: Any) {
    State.global.team = Int(teamNumber.text ?? "0") ?? -1
    State.global.wheels = Int(wheelInput.text ?? "0") ?? -1
    State.global.weight = Int(weightInput.text ?? "0") ?? -1
    State.global.motor = Int(motorInput.text ?? "0") ?? -1
    State.global.comment = String(commentInput.text!)
    State.global.drivetrain = String(driveInput.text!)
    State.global.auto = String(autoInput.text!)
    State.global.program = String(programInput.text!)
    State.global.tele = String(teleInput.text!)
    State.global.hang = String(hangInput.text!)
    State.global.assist = String(assistInput.text!)
        let alert = UIAlertController(title: "Exiting", message: "Are you sure you want to submit?", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .`default`, handler: { _ in
            self.performSegue(withIdentifier: "SubmitSegue", sender: sender)
        }))
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("Cancel", comment: "Default action"), style: .`default`, handler: { _ in
        }))
        
        self.present(alert, animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
          State.global = State()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

