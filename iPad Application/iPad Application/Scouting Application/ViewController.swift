//
//  ViewController.swift
//  Scouting Application
//
//  Created by Vrishab Madduri on 10/30/17.
//  Copyright © 2017 Vrishab Madduri. All rights reserved.
//
import UIKit

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    var startTime: Date? = nil
    var descriptionOptions = [""]
    var assistOptions = [""]
    @IBOutlet weak var matchInput: UITextField!
    @IBOutlet weak var teamInput: UITextField!
    @IBOutlet weak var matchColor: UISegmentedControl!
    @IBOutlet weak var scoreInput: UITextField!
    @IBOutlet weak var commentInput: UITextField!
    @IBOutlet weak var autoscaleInput: UITextField!
    @IBOutlet weak var autoswitchInput: UITextField!
    @IBOutlet weak var lineControl: UISegmentedControl!
    @IBOutlet weak var penaltyControl: UISegmentedControl!
    @IBOutlet weak var AllianceSwitch: UIStepper!
    
    @IBOutlet weak var hangInput: UITextField!
    @IBOutlet weak var startButton: UIButton!
    @IBOutlet weak var pauseButton: UIButton!
    
    @IBAction func failed(_ sender: Any) {
        GlobalState.failureArray[GlobalState.failureArray.count - 1] = true
        
        let timeElapsed = Date().timeIntervalSince(startTime!)
        
        if timeElapsed > 0.5 {
            startButton.titleLabel?.text = "Start Timer"
            GlobalState.timerValues.append(Int(timeElapsed))
        }
        
        startButton.isHidden = false
        startButton.isUserInteractionEnabled = true
        
        pauseButton.isHidden = true
        pauseButton.isUserInteractionEnabled = false
    }
    
    
    @IBAction func start(_ sender: Any) {
        print("starting \(Date())")
        print(startButton.titleLabel)
        GlobalState.failureArray.append(false)
        startTime = Date()
        
        startButton.isHidden = true
        startButton.isUserInteractionEnabled = false
        
        pauseButton.isHidden = false
        pauseButton.isUserInteractionEnabled = true
    }

    @IBAction func pause(_ sender: Any) {
        print("finished")
        
        let timeElapsed = Date().timeIntervalSince(startTime!)
        
        if timeElapsed > 0.5 {
            startButton.titleLabel?.text = "Start Timer"
            GlobalState.timerValues.append(Int(timeElapsed))
        }
        
        pauseButton.isHidden = true
        pauseButton.isUserInteractionEnabled = false
        
        startButton.isHidden = false
        startButton.isUserInteractionEnabled = true
    }
    
    @IBOutlet weak var OpposingSwitch: UIStepper!
    @IBOutlet weak var OpposingSwitchInput: UITextField!
    
    @IBOutlet weak var vaultInput: UITextField!
    @IBAction func vault(_ sender: UIStepper) {
        GlobalState.vault = Int(vaultInput.text ?? "0") ?? 0
        vaultInput.text = String(Int(sender.value) + GlobalState.vault)
        GlobalState.vault = Int(vaultInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBOutlet weak var AllianceSwitchInput: UITextField!
    
    @IBAction func autoScale(_ sender: UIStepper) {
        GlobalState.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        autoscaleInput.text = String(Int(sender.value) + GlobalState.autoscale)
        GlobalState.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBAction func autoSwitch(_ sender: UIStepper) {
        GlobalState.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        autoswitchInput.text = String(Int(sender.value) + GlobalState.autoswitch)
        GlobalState.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBAction func allianceswitchvalueChanged(_ sender: UIStepper) {
    GlobalState.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
    AllianceSwitchInput.text = String(Int(sender.value) + GlobalState.allianceswitch)
    GlobalState.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    @IBOutlet weak var descriptionPicker: UIPickerView!
    
    @IBOutlet weak var assistPicker: UIPickerView!
    @IBAction func opposingallianceswitchChanged(_ sender: UIStepper) {
        GlobalState.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        OpposingSwitchInput.text = String(Int(sender.value) + GlobalState.opposingswitch)
        GlobalState.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        sender.value = 0
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        descriptionOptions = ["left", "center", "right"]
        assistOptions = ["N/A", "Failed", "Assisted"]
        descriptionPicker.delegate = self
        descriptionPicker.dataSource = self
        assistPicker.delegate = self
        assistPicker.dataSource = self
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
   
    @IBAction func submit(_ sender: Any) {
        GlobalState.color = matchColor.titleForSegment(at:  matchColor.selectedSegmentIndex) ?? "No"
        GlobalState.match = Int(matchInput.text ?? "0") ?? -1
        GlobalState.team = Int(teamInput.text ?? "0") ?? -1
        GlobalState.comment = String(commentInput.text!)
        GlobalState.penalty = penaltyControl.titleForSegment(at:  penaltyControl.selectedSegmentIndex) ?? "No"
        GlobalState.line = lineControl.titleForSegment(at:  lineControl.selectedSegmentIndex) ?? "No"
        GlobalState.hang = String(hangInput.text!)
        GlobalState.vault = Int(vaultInput.text ?? "0") ?? 0
        GlobalState.autoscale = Int(autoscaleInput.text ?? "0") ?? 0
        GlobalState.autoswitch = Int(autoswitchInput.text ?? "0") ?? 0
        GlobalState.allianceswitch = Int(AllianceSwitchInput.text ?? "0") ?? 0
        GlobalState.opposingswitch = Int(OpposingSwitchInput.text ?? "0") ?? 0
        
        
         self.performSegue(withIdentifier: "SubmitSegue", sender: self)
        
    }
  
     func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return 3
    }
  
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if pickerView == descriptionPicker {
            GlobalState.pickerView = self.pickerView(pickerView, titleForRow: row, forComponent: component)!
        } else {
            GlobalState.assistView = row - 1
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if(pickerView.tag == 2){
            return "\(descriptionOptions[row])"
        }else{
            return "\(assistOptions[row])"
        }
    }
}

